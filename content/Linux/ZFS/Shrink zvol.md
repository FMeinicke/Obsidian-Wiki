---
publish: true
created: 2025-01-15T16:58:05.976+01:00
modified: 2025-05-26T17:04:04.000+02:00
published: 2025-05-26T17:04:04.000+02:00
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
