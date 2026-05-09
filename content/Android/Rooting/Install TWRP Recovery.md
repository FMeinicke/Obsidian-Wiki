---
publish: true
created: 2024-12-06T06:58:20.967+01:00
modified: 2025-05-26T17:03:23.000+02:00
published: 2025-05-26T17:03:23.000+02:00
---

#twrp #adb #fastboot

> [!info] Source
>
> - <https://www.getdroidtips.com/download-latest-magisk-zip-magisk-manager-root-phone/>

1. Install ADB, Fastboot and Android USB drivers (if necessary) on a PC

2. Download TWRP Recovery from <https://dl.twrp.me>

3. Unlock the bootloader on the device
   1. Enable Developer Mode
      1. Got to Settings > About Phone
      2. Tap the Build Number multiple times until a toast or popup shows up, saying you're now a developer

   2. Go to Developer Settings now and enable OEM Unlocking

   3. Connect the phone to a PC via USB

   4. If the phone runs Android 5.1 or lower run

      ```shell
      fastboot oem unlock
      ```

      for Android 6.0 or higher

      ```shell
      fastboot flashing unlock
      ```

   5. Use the volume buttons to move around in the menu on the phone screen and highlight Yes, then press the power button to confirm

4. Power off the phone

5. Boot into the bootloader (press volume up and the power button simultaneously until the bootloader menu shows up; could also be another combo)

6. Connect the phone to a PC via USB again

7. Flash the downloaded TWRP Recovery image (replace `twrp.img` with the actual file name)

   ```shell
   fastboot flash recovery twrp.img
   ```

8. Once the flashing is done, reboot

   ```shell
   fastboot reboot
   ```
