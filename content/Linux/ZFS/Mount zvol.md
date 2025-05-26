---
{"publish":true,"cssclasses":""}
---


#mount #zvol #kpartx

> [!info] Source(s)
> 
> - <https://forum.proxmox.com/threads/mount-zvol-to-host-ct.118384/>

- run `kpartx` on the zvol device to discover available partitions
- these will show up under `/dev/mapper` and can be mounted as usual

```shell
sudo kpartx -av /dev/zvol/ssd-storage/Test # or /dev/zd16
sudo mount /dev/mapper/Test1 # or /dev/mapper/zd16p1
```