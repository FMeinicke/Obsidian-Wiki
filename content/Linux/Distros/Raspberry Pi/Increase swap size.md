---
{"publish":true,"created":"2025-05-15T09:01:50.139+02:00","modified":"2025-05-26T15:25:09.919+02:00","published":"2025-05-26T15:25:09.919+02:00","cssclasses":""}
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