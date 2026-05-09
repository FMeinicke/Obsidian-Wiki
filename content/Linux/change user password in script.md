---
publish: true
created: 2024-12-06T06:58:21.220+01:00
modified: 2025-05-26T17:03:25.000+02:00
published: 2025-05-26T17:03:25.000+02:00
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
