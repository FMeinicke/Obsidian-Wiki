---
{"publish":true,"cssclasses":""}
---


#zfs/set/volsize #zfs/zvol #vm

> [!info] Source
> 
> - <https://forums.truenas.com/t/how-to-shrink-zvol-used-in-iscsi-via-cli/3306/6>

- make sure that e.g., a VM using this zvol has properly shrunken its partitions and moved all data to the "logical start" of the device
- also ensure that the new zvol size is a bit (couple of MB or 1 GB) larger than the size of the VM's partitions to prevent data loss

```shell
zfs set volsize=32G poolname/zvolname
```
