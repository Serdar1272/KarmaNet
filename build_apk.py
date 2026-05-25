#!/usr/bin/env python3
"""
KarmaNet APK Builder
Buildozer aracılığıyla otomatik APK oluşturma scripti
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Komut çalıştır ve sonucu göster"""
    print(f"\n📦 Çalıştırılıyor: {' '.join(cmd)}\n")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def main():
    print("=" * 50)
    print("🚀 KarmaNet APK İnşa Aracı")
    print("=" * 50)
    
    # Adım 1: Buildozer kurulumu kontrol et
    print("\n1️⃣  Buildozer kontrol ediliyor...")
    try:
        subprocess.run("buildozer --version", shell=True, capture_output=True, check=True)
        print("✅ Buildozer kurulu!")
    except:
        print("❌ Buildozer bulunamadı. Kurulum başlıyor...")
        if not run_command("pip install buildozer"):
            print("❌ Buildozer kurulması başarısız!")
            sys.exit(1)
    
    # Adım 2: Bağımlılıklar kontrol et
    print("\n2️⃣  Gerekli bağımlılıklar kontrol ediliyor...")
    required = ["cython", "pyjnius"]
    for pkg in required:
        try:
            __import__(pkg)
            print(f"✅ {pkg} kurulu!")
        except:
            print(f"⚠️  {pkg} kurulması başlıyor...")
            run_command(f"pip install {pkg}")
    
    # Adım 3: APK oluştur
    print("\n3️⃣  APK inşa ediliyor (Bu 5-10 dakika sürebilir)...")
    print("⏳ Lütfen bekleyin...")
    
    if not run_command("buildozer android debug"):
        print("\n❌ APK inşaası başarısız!")
        sys.exit(1)
    
    # Adım 4: Tamamlandı
    print("\n" + "=" * 50)
    print("✅ APK BAŞARIYLA OLUŞTURULDU!")
    print("=" * 50)
    
    # APK dosyasını bul
    apk_path = None
    bin_dir = "./bin"
    if os.path.exists(bin_dir):
        for file in os.listdir(bin_dir):
            if file.endswith(".apk"):
                apk_path = os.path.join(bin_dir, file)
                break
    
    if apk_path:
        print(f"\n📱 APK Dosyası: {apk_path}")
        print(f"📊 Boyut: {os.path.getsize(apk_path) / (1024*1024):.2f} MB")
        print("\n🎯 Şimdi bunu Android cihazına yükleyebilirsin!")
        print("   Komutu kullan: adb install " + apk_path)
    else:
        print("\n⚠️  APK dosyası bin/ klasöründe bulunamadı.")
        print("   İçeriğini kontrol et: ls -la bin/")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
