---
publish: true
sorting-spec: |-
  ZFS
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Mount zvol](Linux/ZFS/Mount zvol.md)
- [Resize a zvol used by a VM as root disk](Linux/ZFS/Resize a zvol used by a VM as root disk.md)
- [Shrink zvol](Linux/ZFS/Shrink zvol.md)

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



#zfs/set/volsize #zfs/zvol #vm

> [!info] Source
> 
> - <https://forums.truenas.com/t/how-to-shrink-zvol-used-in-iscsi-via-cli/3306/6>

- make sure that e.g., a VM using this zvol has properly shrunken its partitions and moved all data to the "logical start" of the device
- also ensure that the new zvol size is a bit (couple of MB or 1 GB) larger than the size of the VM's partitions to prevent data loss

```shell
zfs set volsize=32G poolname/zvolname
```




#e2fsck #resize2fs #fdisk #zfs/set/volsize #truenas

> [!info] Source
> 
> - <https://askubuntu.com/a/1224578/1152691>
> - <https://www.truenas.com/community/threads/changing-size-shrink-on-active-zvol.42142/post-444130>

- shutdown the VM
- edit the VM to add a live ISO image with the device order higher than the disk device of the VM
- start the VM to boot into the live ISO
- resize the root partition to its new smaller size
    - run `e2fsck -f /dev/vda3` (where `dev/vda3` is the partition to be resized)
    - then run `resize2fs /dev/vda3 150G` to resize the partition (where `150G` is the new smaller size)
- alter the partition table
    - run `fdisk /dev/vda`
    - enter `p` to print the table for reference
    - enter `d` followed by `3` to delete the partition
    - enter `n` followed by `3` followed by `+150G` to create a new partition with the smaller size
    - answer `no` if asked to remove the ext4 marker
    - enter `t` followed by the correct partition type ID (in this case `23` for `Linux root (x86-64)`)
    - enter `w` to write the new partition table
- shutdown the VM again
- create a ZFS snapshot of the zvol
- resize the zvol (only possible via the command line)
    - run `zfs set volsize=200G <pool>/<zvol>` to set the new size for the zvol
    - this will destroy the partition table and maybe even the whole data, but we can get that back when we...
- restore the snapshot from before (this can be done in the GUI again), confirming that this will delete/replace all data
- ~~the size of the zvol will stay the new smaller size, but~~ all data (since it should fit snugly into the new space) will be restored
- then simply start the VM and enjoy

> [!NOTE] Edit
> It seems, the restoration of the snapshot did reset the `volsize` as well, however, I still have much more free space than before.
> Also, the partition table and size of the disk inside the VM is still the new smaller size.



---

## Tagged mentions


