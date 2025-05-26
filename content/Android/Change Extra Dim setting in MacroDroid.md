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
