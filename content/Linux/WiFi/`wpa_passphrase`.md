---
publish: true
created: 2024-12-06T06:58:23.623+01:00
modified: 2025-05-26T17:03:49.000+02:00
published: 2025-05-26T17:03:49.000+02:00
---

#wpa #wpa_cli #wpa_supplicant #passphrase #wifi #network

> [!info] Source

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
