---
{"publish":true,"cssclasses":""}
---

#adb/install

> [!info] Source(s)
> 
> - <https://www.macrodroidforum.com/index.php?threads/macrodroid-helper-apk.1/>
> - <https://www.macrodroidforum.com/index.php?threads/installing-helper-on-android-14.5606/>

- download the APK
- connect to the phone (see above) --> `adb devices` should show the device
- run `adb install --bypass-low-target-sdk-block FILENAME.apk`
- afterward run `adb shell pm grant com.arlosoft.macrodroid.helper android.permission.WRITE_SECURE_SETTINGS`