---
{"publish":true,"title":"Make `/sys/power/image_size` persistent","created":"2025-05-15T09:01:50.311+02:00","modified":"2025-05-26T15:42:21.495+02:00","published":"2025-05-26T15:42:21.495+02:00","cssclasses":""}
---


#swap #hibernation #sys/power/image_size #tmpfiles

> [!info] Source(s)
> 
> - <https://wiki.archlinux.org/title/Power_management/Suspend_and_hibernate#About_swap_partition/file_size>
> - <https://docs.kernel.org/admin-guide/pm/sleep-states.html?highlight=image_size#basic-sysfs-interfaces-for-system-suspend-and-hibernation>
> - <https://docs.kernel.org/power/swsusp.html>
> - <https://www.reddit.com/r/archlinux/comments/ftak2a/comment/fm5y7v4/>
> - <https://www.reddit.com/r/Gentoo/comments/p7dckk/comment/h9laczr/>

- non-persistent

```shell
echo 0 | sudo tee /sys/power/image_size
```

- persistent

```shell
sudo vim /etc/tmpfiles.d/hibernation_image_size.conf

#    Path                   Mode UID  GID  Age Argument
w    /sys/power/image_size  -    -    -    -   0
```