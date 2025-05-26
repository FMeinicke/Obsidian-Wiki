---
{"publish":true,"cssclasses":""}
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