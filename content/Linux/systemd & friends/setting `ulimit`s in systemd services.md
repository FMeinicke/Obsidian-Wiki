---
publish: true
created: 2024-12-06T06:58:11.967+01:00
modified: 2025-05-26T17:02:27.000+02:00
published: 2025-05-26T17:02:27.000+02:00
---

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
