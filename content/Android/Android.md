---
publish: true
sorting-spec: |-
  Android
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Allow restricted settings for side-loaded app](Android/Allow restricted settings for side-loaded app.md)
- [Change Extra Dim setting in MacroDroid](Android/Change Extra Dim setting in MacroDroid.md)
- [Install MacroDroid Helper APK via `adb`](Android/Install MacroDroid Helper APK via `adb`.md)
- [Wireless debugging](Android/Wireless debugging.md)
- [Rooting](Rooting)
    - [Install Magisk using TWRP](Android/Rooting/Install Magisk using TWRP.md)
    - [Install TWRP Recovery](Android/Rooting/Install TWRP Recovery.md)

---



#android/accessibility #android/settings/restricted #android/app-info

> [!info] Source
> 
> - <https://stackoverflow.com/a/72217217/12780516>

1. Go to app info.
2. Tap on 3 dots.
3. Choose "allow restricted settings".
4. Enter your lock code.



#adb/pair #adb/connect

> [!info] Source(s)
> 
> - <https://stackoverflow.com/a/67556359/12780516>

- on the phone
    - enable developer options
    - enable wireless debugging in the developer options
    - select "Pair new device with pairing code"
- on the PC
    - install ADB
    - run `adb pair <IP>:<PORT>` where `<IP>` and `<PORT>` are the IP address and port shown on the phone
    - enter the pairing code shown on the phone
    - now you can `adb connect <IP>:<PORT>` (note that the port is different from the one used during pairing)


#adb/install

> [!info] Source(s)
> 
> - <https://www.macrodroidforum.com/index.php?threads/macrodroid-helper-apk.1/>
> - <https://www.macrodroidforum.com/index.php?threads/installing-helper-on-android-14.5606/>

- download the APK
- connect to the phone (see above) --> `adb devices` should show the device
- run `adb install --bypass-low-target-sdk-block FILENAME.apk`
- afterward run `adb shell pm grant com.arlosoft.macrodroid.helper android.permission.WRITE_SECURE_SETTINGS`

---
publish: true
title: Change "Extra Dim" setting in MacroDroid
cssclasses:
  - hide_properties
---

#android/settings/secure #android/accessibility/extra-dim #macrodroid/adb-hack #macrodroid/system-setting #adb

> [!info] Source
> 
> - <https://www.reddit.com/r/macrodroid/comments/sl9h7e/comment/hvsm8gz/>

- grant `WRITE_SECURE_SETTINGS` permission to MacroDroid using `adb`
- use the *System Setting* macro to write the **Secure** setting with the key `reduce_bright_colors_activated`
    - 0 = Extra Dim off
    - 1 = Extra Dim on
    - don't check "Use Helper App" for Android >= 15 (do check it for until Android 14)


---

## Tagged mentions


