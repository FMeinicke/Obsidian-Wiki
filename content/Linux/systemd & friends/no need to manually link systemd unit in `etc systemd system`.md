---
publish: true
title: no need to manually link systemd unit in `/etc/systemd/system`
---

#systemd #systemd-unit #systemd-service

> [!info] Source
>
>

```shell
$ sudo systemctl link ~/path/to/unit@.service
$ sudo systemctl enable unit@instance
Created symlink /etc/systemd/system/default.target.wants/user@instance.service → /home/pi/sila_cetoni/raspi/systemd/user@.service.
Created symlink /etc/systemd/system/multi-user.target.wants/user@instance.service → /home/pi/sila_cetoni/raspi/systemd/user@.service.
Created symlink /etc/systemd/system/user@instance.service → /home/user/path/to/unit@.service.
```