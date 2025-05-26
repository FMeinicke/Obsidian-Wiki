---
{"publish":true,"cssclasses":""}
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