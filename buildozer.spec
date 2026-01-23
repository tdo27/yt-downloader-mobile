[app]
title = YT Music Downloader
package.name = ytmusicdownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# REQUIREMENTS (Am adaugat cython aici)
requirements = python3,kivy==master,yt-dlp,cython

orientation = portrait
permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# ANDROID SETTINGS (Aici am adaugat ce lipsea pentru succes)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
android.archs = arm64-v8a

# LOG LEVEL (2 pentru a vedea erorile clar)
log_level = 2

[buildozer]
bin_dir = ./bin


