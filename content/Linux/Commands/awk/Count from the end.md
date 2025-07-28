---
{"publish":true,"created":"2025-05-15T09:01:49.310+02:00","modified":"2025-05-26T15:25:07.872+02:00","published":"2025-05-26T15:25:07.872+02:00","cssclasses":""}
---


#awk/print #awk/nf

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/64674/482223>

```shell
echo "This is a test" | awk '{ print$(NF-2) }'
is
```