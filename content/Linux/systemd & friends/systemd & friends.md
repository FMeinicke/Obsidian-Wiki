---
publish: true
sorting-spec: |-
  systemd & friends
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Change `journalctl`'s pager options](Linux/systemd & friends/Change `journalctl`'s pager options.md)
- [Escape specifiers in systemd files](Linux/systemd & friends/Escape specifiers in systemd files.md)
- [Managing multiple instances of a systemd template service](Linux/systemd & friends/Managing multiple instances of a systemd template service.md)
- [no need to manually link systemd unit in `etc systemd system`](Linux/systemd & friends/no need to manually link systemd unit in `etc systemd system`.md)
- [setting `ulimit`s in systemd services](Linux/systemd & friends/setting `ulimit`s in systemd services.md)
- [systemd network files](Linux/systemd & friends/systemd network files.md)
- [systemd service depending on a network interface](Linux/systemd & friends/systemd service depending on a network interface.md)

---

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


#systemd #systemd-service #ulimit

> [!info] Source
>
> - `man 5 systemd.exec`
> - <https://man.archlinux.org/man/systemd.exec.5.en>

```
Directive        ulimit equivalent     Unit
LimitCPU=        ulimit -t             Seconds
LimitFSIZE=      ulimit -f             Bytes
LimitDATA=       ulimit -d             Bytes
LimitSTACK=      ulimit -s             Bytes
LimitCORE=       ulimit -c             Bytes
LimitRSS=        ulimit -m             Bytes
LimitNOFILE=     ulimit -n             Number of File Descriptors
LimitAS=         ulimit -v             Bytes
LimitNPROC=      ulimit -u             Number of Processes
LimitMEMLOCK=    ulimit -l             Bytes
LimitLOCKS=      ulimit -x             Number of Locks
LimitSIGPENDING= ulimit -i             Number of Queued Signals
LimitMSGQUEUE=   ulimit -q             Bytes
LimitNICE=       ulimit -e             Nice Level
LimitRTPRIO=     ulimit -r             Realtime Priority
LimitRTTIME=     ulimit -R             Microseconds
```


#systemd #systemd-network #systemd-service

> [!info] Source
>
>

- by default `ProtectHome=yes` (`man systemd-exec(5)`)
- changing to `ProtectHome=read-only` in override config fixes


#systemd #systemd-service #service-template #instanced-service

> [!info] Source
>
>

- Use the `<service_name>*` syntax to operate on all services of the `<service_name>@.service` template, e.g.

  ```shell
  sudo systemctl start 'sila_cetoni*'
  ```

  will start all instanced services of the `sila_cetoni@.service` template
- this works for the systemd commands `start`, `stop`, `restart` and `status` (maybe for others too but this has not been tested yet)


#systemd #journalctl #less

> [!info] Source
>
>

- set the `SYSTEM_LESS` environment variable
- by default this value is `FRSXMK`
- when overriding the variable be sure to include all of the desired default options as well
- to decrease the default horizontal scroll size, for example: `export SYSTEMD_LESS="FRSXMK -# 10"` (will scroll by 10 characters for each right/left arrow key press)


#systemd #systemd-unit #systemd-service #network

> [!info] Source
>
> - <https://unix.stackexchange.com/a/227768>

- use `BindsTo=` and `After=` in the `[Unit]` section and `WantedBy=` in `[Install]`

  ```systemd
  [Unit]
  Description=Service depending on interface %I
  Wants=network-online.target
  BindsTo=sys-subsystem-net-devices-%i.device
  After=multi-user.target sys-subsystem-net-devices-%i.device network-online.target

  [Service]
  Type=simple
  ExecStart=...

  [Install]
  WantedBy=default.target sys-subsystem-net-devices-%i.device
  ```

- use `Wants=network-online.target` and `After=network-online.target` to actually wait for the network to be online
  > [!NOTE]
  > This only works as a one-time concept during system start-up. The `network-online.service` unit does not monitor the online state of the system!



#systemd/specifier 

> [!info] Source
> 
> - <https://stackoverflow.com/a/54737279/12780516>
> - [`man systemd.unit`](https://man7.org/linux/man-pages/man5/systemd.unit.5.html#:~:text=use%20%22%25%25%22%20in%20place%20of%20%22%25%22)

- use `T` if you want to use `%T` as the format specifier for the `date` command instead of `%T` as the specifier for the temporary directory


---

## Tagged mentions


