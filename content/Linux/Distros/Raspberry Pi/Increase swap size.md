---
publish: true
created: 2024-12-06T06:58:17.334+01:00
modified: 2025-05-26T17:03:00.000+02:00
published: 2025-05-26T17:03:00.000+02:00
---

#swap #dphys-swapfile #swapon #swapoff

> [!info] Source
>
> - <https://diyusthad.com/2022/01/how-to-increase-swap-size-in-raspberry-pi.html>

```shell
sudo dphys-swapfile swapoff
sudo vim /etc/dphys-swapfile
#change CONF_SWAPSIZE= to a value in MB
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```
