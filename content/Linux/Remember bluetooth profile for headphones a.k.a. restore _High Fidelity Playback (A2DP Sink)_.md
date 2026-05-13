---
publish: true
created: 2025-05-15T09:01:50.342+02:00
modified: 2025-05-26T17:11:27.703+02:00
published: 2025-05-26T17:11:27.703+02:00
cssclasses: ""
---


#pulseaudio #bluetooth/profile/restore #bluetooth/high-fidelity #bluetooth/a2dp-sink

> [!info] Source(s)
> 
> - <https://askubuntu.com/a/1413936/1152691>
> - <https://askubuntu.com/a/1307375/1152691>

- create a file called e.g. `restore-bluetooth-profile.pa` in `/etc/pulse/default.pa.d/` with the following content

```
load-module module-card-restore restore_bluetooth_profile=true
```

- ensure that in `/etc/pulse/default.pa` there is no line that also loads `module-card-restore`
    - if there is, comment it out (or remove it), since pulseaudio will not load the same module twice, thus not respecting our custom option
- then [[Linux/Restart pulseaudio\|restart pulseaudio]]

**OR**

- edit `/etc/pulse/default.pa` and find the entry `load-module module-bluetooth-policy` (it should be guarded by an `.ifexists` as seen below)
- add `auto_switch=2`

```conf
.ifexists module-bluetooth-policy.so
load-module module-bluetooth-policy auto_switch=2
.endif
```

- then [[Linux/Restart pulseaudio\|restart pulseaudio]]
