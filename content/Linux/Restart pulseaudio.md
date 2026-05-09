---
publish: true
created: 2024-12-06T06:58:24.433+01:00
modified: 2025-05-26T17:04:42.000+02:00
published: 2025-05-26T17:04:42.000+02:00
---

#pulseaudio/check #pulseaudio/kill #pulseaudio/start #systemctl/user #systemctl/restart #systemctl/status

> [!info] Source(s)
>
> - <https://askubuntu.com/questions/15223/how-can-i-restart-pulseaudio-without-having-to-logout>

- either using the `pulseaudio` command

```shell
pulseaudio --check     # exit status 0 means daemon is running
pulseaudio --kill      # kill running daemon
pulseaudio --start     # start daemon
```

- or by using `systemctl` (must use `--user`!)

```shell
systemctl --user restart pulseaudio
systemctl --user status pulseaudio
```
