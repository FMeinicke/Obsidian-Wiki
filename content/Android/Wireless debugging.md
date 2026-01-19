---
publish: true
created: 2025-05-15T09:01:46.169+02:00
modified: 2025-05-26T15:25:01.058+02:00
published: 2025-05-26T15:25:01.058+02:00
cssclasses: ""
---

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