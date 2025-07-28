---
{"publish":true,"created":"2025-05-15T09:01:50.748+02:00","modified":"2025-05-26T15:25:11.919+02:00","published":"2025-05-26T15:25:11.919+02:00","cssclasses":""}
---


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