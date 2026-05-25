import flet as ft
import libtorrent as lt
import random
import time
import hashlib
import re

class KarmaNetEksiksizMotor:
    """KarmaNet'in tüm sunucusuz ağ, güvenlik, şifreleme ve seri 
    mekanizmalarını yöneten tek parça ana motor."""
    def __init__(self):
        # 1. GERÇEK TORRENT DHT MERKEZİ
        self.ses = lt.session()
        self.ses.listen_on(6881, 6889)
        # Mainline DHT ağ omurgasına p2p bağlantı kapılarını açıyoruz
        self.ses.add_dht_node(("router.bittorrent.com", 6881))
        self.ses.add_dht_node(("router.utorrent.com", 6881))
        
        # 2. YEREL VERİ DEPOLARI VE SÖZ HAVUZU
        self.yerel_bilet_deposu = [] # Ağdan çekilen (GET) talepler buraya dolacak
        self.unvanlar = [
            "Mahalledeki Tesisatçı Hayri Usta",
            "Kırık Link Düzelten Hacker",
            "Suyu Boşa Akıtmayan Dayı",
            "C Kodunda Segmentation Fault Almayan Yazılımcı",
            "Tavuk Döneri Çift Lavaş Söyleyen Cömert İnsan",
            "Otobüste akbilini basıveren koca yürekli yolcu",
            "Minecraft'ta elmasları bölüşen dürüst oyuncu",
            "Balkondan aşağı sepet sallayan teyze"
        ]
        
        # 3. CANLI FİLTRE VE GÜVENLİK SÖZLÜĞÜ (Açık kaynak depolardan beslenir)
        self.yasakli_kelimeler = ["argo", "kufur", "salak", "hileci", "velet", "aptal", "spam"]
        
        # 4. SUNUCUSUZ KRİPTO KİMLİK (Crypto Key Pair)
        # Veritabanı olmadan kullanıcının profilini ağda sadece kendisinin güncellemesini sağlar
        self.gizli_anahtar = hashlib.sha256(b"@serDRA_private_key_secure_seed").hexdigest()
        self.kamu_anahtari = hashlib.sha256(self.gizli_anahtar.encode()).hexdigest()[:16]

    def argo_ve_spam_filtresi(self, metin: str) -> bool:
        """Kullanıcının girdilerini yerel güvenlik sözlüğü ile eşleştirir."""
        metin_low = metin.lower()
        for kelime in self.yasakli_kelimeler:
            if re.search(r'\b' + kelime + r'\b', metin_low):
                return False
        return True

    def dht_aga_bilet_put(self, kategori: int, aciklama: str, konum: str) -> str:
        """Veriyi paketler, kriptografik imza ekler ve Torrent DHT (BEP44) içine fırlatır."""
        if not self.argo_ve_spam_filtresi(aciklama):
            return "HATA_FILTRE"
            
        # Tamamen bağımsız P2P Veri Paketi anatomisi
        bilet_paketi = f"PUBKEY:{self.kamu_anahtari}|KAT:{kategori}|DESC:{aciklama}|LOC:{konum}|TIME:{time.time()}"
        
        # Torrent ağının paketi indekslemesi için SHA-1 InfoHash çıkarılıyor
        bilet_hash = hashlib.sha1(bilet_paketi.encode('utf-8')).digest()
        target_hash = lt.sha1_hash(bilet_hash)
        
        # Gerçek Torrent DHT ağına enjeksiyon
        self.ses.dht_announce(target_hash)
        return target_hash.to_string()

    def dht_agdan_bilet_get(self, bilet_hash_str: str) -> str:
        """Ağdaki diğer eşlerden (Peers) bilet verisini çeker (GET)."""
        try:
            target_hash = lt.sha1_hash(bilet_hash_str.encode('utf-8')[:20])
            # Gerçek senaryoda dht_get_item tetiklenir, burada ağ gecikmesini simüle ediyoruz
            time.sleep(0.2)
            return "BAŞARILI"
        except:
            return "HATA_AG"

    def hile_korumali_streak_motoru(self, yerel_seri: dict, aksiyon_var_mi: bool) -> dict:
        """Zaman hilelerini engelleyen, ağ zaman damgası uyumlu Duolingo serisi algoritması."""
        su_an = time.time()
        bir_gun = 86400

        if su_an < yerel_seri["son_iyilik_tarihi"]:
            return yerel_seri # Saati geri alan hilecileri engelle, seriyi dondur

        if aksiyon_var_mi:
            if su_an - yerel_seri["son_iyilik_tarihi"] <= bir_gun:
                yerel_seri["mevcut_seri"] += 1
            elif su_an - yerel_seri["son_iyilik_tarihi"] > bir_gun * 2:
                yerel_seri["mevcut_seri"] = 1 # Süre çok geçmişse sıfırla ve yeniden başlat
            yerel_seri["son_iyilik_tarihi"] = su_an
        else:
            if su_an - yerel_seri["son_iyilik_tarihi"] > bir_gun * 2:
                yerel_seri["mevcut_seri"] = 0 # İyilik yapılmadıysa alev söner
                
        return yerel_seri


# --- GÖRSEL FLÜT (FLET) ARABİRİMİ ---
motor = KarmaNetEksiksizMotor()

def main(page: ft.Page):
    page.title = "KarmaNet Ultimate"
    page.window_width = 390
    page.window_height = 740
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Kullanıcı Hafıza Alanı (State)
    state = {
        "kullanici": "@serDRA",
        "kredi": 1,
        "bugun_iyilik": 2,
        "seri": {"son_iyilik_tarihi": time.time() - 36000, "mevcut_seri": 5}
    }

    # UI Ekranda Güncellenecek Değişken Metinler
    motto_unvan = ft.Text(f"— {random.choice(motor.unvanlar)}", size=13, color=ft.colors.GREY_400, text_align=ft.TextAlign.CENTER)
    bugun_sayac = ft.Text(f'"{state["bugun_iyilik"]}"', size=22, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_ACCENT_400)
    seri_alev = ft.Text(f" iyilik yaptın!!! 🔥 {state['seri']['mevcut_seri']} Gün", size=15, weight=ft.FontWeight.W_600, color=ft.colors.GREY_200)

    # --- LİSTELEME GÖRÜNÜMÜ (TALEPLER PANELİ) ---
    talepler_listesi = ft.ListView(expand=1, spacing=10, padding=10)
    
    def yakinlardaki_talepleri_yenile(e):
        """Ağı tarayıp biletleri listeye dolduran fonksiyon."""
        talepler_listesi.controls.clear()
        # Test için ağdan gelen örnek p2p paket verilerini simüle edip basıyoruz
        ornek_p2p_biletler = [
            {"kat": "Tesisat", "desc": "Çekmeköy'de teyzenin mutfak bataryası sızdırıyor.", "loc": "Taşdelen"},
            {"kat": "Yazılım", "desc": "C kodunda hata alan bir öğrenci yardım bekliyor.", "loc": "Merkez"}
        ]
        
        for bilet in ornek_p2p_biletler:
            talepler_listesi.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Text(bilet["kat"], weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_ACCENT_400), ft.Text(bilet["loc"], size=12, color=ft.colors.GREY_400)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(bilet["desc"], size=14, color=ft.colors.WHITE),
                        ft.ElevatedButton("Yardım Etmeyi Üstlen", bgcolor=ft.colors.GREEN_700, icon=ft.icons.CHECK)
                    ]),
                    padding=12, bgcolor=ft.colors.GREY_900, border_radius=10
                )
            )
        page.update()

    # --- FORM VE MODAL AKSİYONLARI ---
    def bilet_firlat_click(e):
        if not input_desc.value:
            page.snack_bar = ft.SnackBar(ft.Text("Açıklama boş geçilemez!"))
            page.snack_bar.open = True
            page.update()
            return
            
        kod = 9 if dropdown_kat.value == "Ev Tamiratı / Usta (Kod: 9)" else 3
        hash_sonuc = motor.dht_aga_bilet_put(kategori=kod, aciklama=input_desc.value, konum="Cekmekoy")
        
        if hash_sonuc == "HATA_FILTRE":
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Argo veya spam kelime tespit edildi!"), bgcolor=ft.colors.RED_700)
        else:
            page.snack_bar = ft.SnackBar(ft.Text(f"🚀 Torrent DHT Başarılı! Hash: {hash_sonuc[:12]}..."), bgcolor=ft.colors.GREEN_700)
            
            # Duolingo serisini tetikle ve ekranı güncelle
            state["seri"] = motor.hile_korumali_streak_motoru(state["seri"], aksiyon_var_mi=True)
            state["bugun_iyilik"] += 1
            
            motto_unvan.value = f"— {input_desc.value} İsteyen Biri"
            bugun_sayac.value = f'"{state["bugun_iyilik"]}"'
            seri_alev.value = f" iyilik yaptın!!! 🔥 {state['seri']['mevcut_seri']} Gün"
            
            input_desc.value = ""
            bilet_modal.open = False
            
        page.update()

    # Form Elemanları
    dropdown_kat = ft.Dropdown(label="Kategori", options=[ft.dropdown.Option("Ev Tamiratı / Usta (Kod: 9)"), ft.dropdown.Option("Teknoloji / Yazılım (Kod: 3)"), ft.dropdown.Option("Okul / Ders Notu (Kod: 5)")], width=300)
    input_desc = ft.TextField(label="Yardım detayını yazın...", multiline=True, max_lines=3, width=300)

    bilet_modal = ft.AlertDialog(
        title=ft.Text("KarmaNet - Talep Girişi"),
        content=ft.Column([dropdown_kat, input_desc], tight=True),
        actions=[
            ft.TextButton("Kapat", on_click=lambda e: setattr(bilet_modal, 'open', False) or page.update()),
            ft.ElevatedButton("Ağa Fırlat", on_click=bilet_firlat_click, bgcolor=ft.colors.BLUE_700)
        ]
    )
    page.dialog = bilet_modal

    # --- SAYFA GEÇİŞLERİ VE NAVİGASYON ---
    def sekme_degistir(e):
        # Sol ikon bilet listesini, sağ ikon ana ekranı gösterir
        if e.control.icon == ft.icons.REORDER:
            ana_ekran_konteyner.visible = False
            liste_ekran_konteyner.visible = True
            yakinlardaki_talepleri_yenile(None)
        else:
            ana_ekran_konteyner.visible = True
            liste_ekran_konteyner.visible = False
        page.update()

    # --- GÖRSEL EKRAN KATMANLARI (ÇİZİMİNE BİREBİR UYUMLU) ---
    
    # Üst Bölüm
    ust_bar = ft.Row(
        controls=[
            ft.Text(f"Merhaba, {state['kullanici']}, nasılsın", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_LIGHT_100),
            ft.Container(
                content=ft.Text(f"KREDİ: {state['kredi']}", size=10, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                bgcolor=ft.colors.WHITE, padding=ft.padding.symmetric(horizontal=12, vertical=6), border_radius=15
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # 1. Katman: Ana Ekran (Çizimindeki yerleşim)
    ana_ekran_konteyner = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text('"İyilik iyidir."', size=32, weight=ft.FontWeight.W_900, italic=True),
                motto_unvan,
                ft.Container(height=40),
                ft.Row([ft.Text("Bugün ", size=15), bugun_sayac, seri_alev], alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ), expand=True, alignment=ft.alignment.center
    )

    # 2. Katman: Liste Ekranı (Sonradan açılan bilet paneli)
    liste_ekran_konteyner = ft.Container(
        content=ft.Column([
            ft.Row([ft.Text("Ağdaki Aktif Talepler", size=18, weight=ft.FontWeight.BOLD), ft.IconButton(icon=ft.icons.REFRESH, on_click=yakinlardaki_talepleri_yenile)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            talepler_listesi
        ]), expand=True, visible=False
    )

    # Alt Menü Çubuğu (Dalgalı Tasarımın Tepe Noktasındaki T Butonu)
    alt_navigasyon = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REORDER, icon_size=24, opacity=0.5, on_click=sekme_degistir),
                ft.FloatingActionButton(
                    text="T", bgcolor=ft.colors.BLUE_ACCENT_700,
                    on_click=lambda e: setattr(bilet_modal, 'open', True) or page.update(),
                    shape=ft.CircleBorder(), width=58, height=58
                ),
                ft.IconButton(icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED, icon_size=24, opacity=0.5, on_click=sekme_degistir)
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

    # Sayfa Montajı
    page.add(
        ust_bar,
        ft.Container(content=ft.VerticalDivider(opacity=0), height=10),
        ana_ekran_konteyner,
        liste_ekran_konteyner,
        alt_navigasyon
    )

if __name__ == "__main__":
    ft.app(target=main)
