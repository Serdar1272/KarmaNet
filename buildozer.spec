[app]

# (str) Title of your application
title = KarmaNet

# (str) Package name
package.name = karmanet

# (str) Package domain (needed for android/ios packaging)
package.domain = org.karmanet

# (source.dir) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.png

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / APP will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use the Apache Commons Lang Java library (required for better WebView
# support on Android 4.0+)
android.apache_ant_version = 1.9.4

# (bool) indicates whether the app uses modern android.app.Activity
# or android.app.Service (the latter is used when service or bootstrap is used)
# Defaults to False
#android.uses_legacy_toolchain = False

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support. This requires android.api >= 28
android.enable_androidx = True

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_src =

# (list) List of Java files for adding pyjnius bindings. You can use only .java
# files, the .aidl will be converted to .java automatically.
#android.add_src =

# (list) Gradle dependencies (maven jar files)
#android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, the app will be viewed as a game. (int) OUYA Console
# rating. Should be one of EVERYONE, TEEN, MATURE, ADULTS_ONLY, UNRATED, or PENDING.
#android.ouya_category = GAME
#android.ouya_category_rating = EVERYONE

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.archs = arm64-v8a

# (int) overrides automatic versionCode generation in buildozer.spec
#android.version_code = 1

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Android features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 30

# (str) Android NDK version to use
#android.ndk = 23c

# (bool) Use the `uses-library` manifest feature to declare that the app uses the androidx
# library (requires android.api >= 28 and androidx). This will prevent some java exceptions in
# Android 12+ when the androidx library is not installed on the device as the app expects.
#android.uses_library = False

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) Android app theme, default is ok for Kivy-based app
#android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_src =

# (list) List of Java files for adding pyjnius bindings. You can use only .java
# files, the .aidl will be converted to .java automatically.
#android.add_src =

# (list) Gradle dependencies (maven jar files)
#android.gradle_dependencies =

# (str) python-for-android release (optional, defaults to the latest stable version)
p4a.release = 2023.06.06

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask
# server on bootstrap flask server to run on 8270 instead of default 5000)
#p4a.port =

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (str) python-for-android directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) python-for-android bootstrap to use, defaults to sdl2
#p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask
# server to run on 8270 instead of default 5000)
#p4a.port =

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya_icon_filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration within the manifest. See the
# documentation for more information on the API.
#android.backup_xml_declaration = <?xml version="1.0" encoding="utf-8"?>...

# (str) Content provider authorities (optional).
# Allows to use the ContentProvider Java object in JNI with pyjnius, either only the classes
# from the standard library or any Java class. See the documentation for the access to JNI and to
# understand the purpose of the ContentProvider.
#android.content_providers =

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display advance warning on buildozer version
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin

#
# Windows specific
#

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, the app will be viewed as a game. (int) OUYA Console
# rating. Should be one of EVERYONE, TEEN, MATURE, ADULTS_ONLY, UNRATED, or PENDING.
#android.ouya_category = GAME
#android.ouya_category_rating = EVERYONE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientations. Possible values are: landscape, sensorLandscape, portrait or sensorPortrait
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

# (list) Android features
#android.features =

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

#
# iOS specific
#

# (bool) Indicate if the application should be fullscreen or not
#ios.fullscreen = True

[requirements]

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
python3
kivy
flet
