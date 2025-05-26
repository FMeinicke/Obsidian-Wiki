---
publish: true
sorting-spec: |-
  WiFi
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [`wpa_passphrase`](Linux/WiFi/`wpa_passphrase`.md)
- [Connect to 2.4 GHz WiFi](Linux/WiFi/Connect to 2.4 GHz WiFi.md)

---



#wpa #wpa_cli #wpa_supplicant #passphrase #wifi #network

> [!info] Source
>
>

```shell
$ wpa_passphrase <SSID>
#reading passphrase from stdin
<ENTER PASSPHRASE>⏎
network={
        ssid="<SSID>"
        #psk="<PASSPHRASE>"
        psk=07d57d914e1b88b356fd6bf12f6d2b3d168a1f94f0ba97daae9391d0cb342151
}
```

Note that the SSID has to match the actual SSID of the WiFi, otherwise the PSK will be wrong and connection to the WiFi will fail.



#wifi #wpa_supplicant #wpa #wpa_cli #network

> [!info] Source
>
>

- find the BSSID for the 2.4 GHz WiFi

  ```shell
  wpa_cli -i wlan0
    Copyright (c) 2004-2019, Jouni Malinen <j@w1.fi> and contributors

  This software may be distributed under the terms of the BSD license.

  See README for more details.

  Interactive mode

  > list_networks

  network id / ssid / bssid / flags

  0       CetoniWLAN      any     [CURRENT]

  > scan_networks

  Unknown command 'scan_networks'

  > scan_network

  Unknown command 'scan_network'

  > scan

  scan           scan_interval  scan_results

  > scan

  OK

  <3>CTRL-EVENT-SCAN-STARTED

  <3>CTRL-EVENT-SCAN-RESULTS

  > scan_results

  bssid / frequency / signal level / flags / ssid

  da:21:f9:76:06:c7       5220    -79     [WPA2-PSK+SAE+FT/PSK-CCMP][ESS] CetoniGuests

  e2:21:f9:76:06:c7       5220    -79     [WPA2-PSK-CCMP][ESS]

  de:21:f9:76:06:c7       5220    -78     [WPA2-PSK-CCMP][ESS]

  d6:21:f9:76:06:c7       5220    -76     [WPA2-PSK+SAE+FT/PSK-CCMP][ESS] CetoniWLAN

  de:21:f9:76:06:c6       2437    -78     [WPA2-PSK-CCMP][ESS]

  d0:21:f9:76:06:c6       2437    -82     [WPA2-PSK+SAE+FT/PSK-CCMP][ESS] CetoniWLAN

  ```
- add an entry in `wpa_supplicant.conf` with that BSSID and add `scan_ssid=1`
  ```conf
  network={
        ssid="CetoniWLAN"
        bssid=d0:21:f9:76:06:c6
        scan_ssid=1
        #psk="<PASSPHRASE>"
  }
  ```

---

## Tagged mentions


