---
{"publish":true,"created":"2025-05-15T09:01:50.873+02:00","modified":"2025-05-26T15:25:07.778+02:00","published":"2025-05-26T15:25:07.778+02:00","cssclasses":""}
---


#passwd

> [!info] Source(s)
> 
> - <https://unix.stackexchange.com/a/197456/482223>

```shell
yes newpassword | passwd someuser
```

if using bash, then `chpasswd` is also an option

```bash
echo "someuser:newpassword" | chpasswd
```