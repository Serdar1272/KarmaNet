@echo off
REM KarmaNet APK Builder - Basit tıklamalı kurulum
REM Kullanıcı sadece bu dosyayı çalıştırsın, geri kalanı otomatik

setlocal enabledelayedexpansion

color 0A
cls

echo.
echo ============================================
echo     KARMANET APK BUILDER
echo ============================================
echo.

REM Python kurulu mu kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python yüklü değil!
    echo Lütfen Python 3.9+ yükleyip tekrar çalıştırın.
    pause
    exit /b 1
)

echo [✓] Python bulundu

REM Buildozer yüklü mü kontrol et
python -m pip show buildozer >nul 2>&1
if errorlevel 1 (
    echo [!] Buildozer kurulması gerekiyor...
    echo.
    python -m pip install --upgrade pip
    python -m pip install buildozer cython pyjnius
    if errorlevel 1 (
        echo [HATA] Buildozer kurulması başarısız!
        pause
        exit /b 1
    )
    echo [✓] Buildozer başarıyla kuruldu
)

echo [✓] Buildozer bulundu
echo.
echo ============================================
echo     APK İNŞA BAŞLANIYOR...
echo     (Bu 5-15 dakika sürebilir)
echo ============================================
echo.

REM APK oluştur
buildozer android debug

if errorlevel 1 (
    echo.
    echo [HATA] APK oluşturulurken hata oluştu!
    echo Lütfen logs klasöründeki hataları kontrol edin.
    pause
    exit /b 1
)

echo.
echo ============================================
echo     [✓] APK BAŞARIYLA OLUŞTURULDU!
echo ============================================
echo.

REM APK dosyasını bul ve göster
for /f "delims=" %%A in ('dir /b bin\*.apk 2^>nul') do (
    set APK_FILE=%%A
    goto found
)

:found
if defined APK_FILE (
    echo APK Dosyası: bin\%APK_FILE%
    echo.
    echo [→] Android cihazınıza yüklemek için:
    echo     adb install bin\%APK_FILE%
    echo.
) else (
    echo [!] APK dosyası bulunamadı, lütfen logs kontrol edin.
)

echo.
pause
