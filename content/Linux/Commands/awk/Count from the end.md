---
publish: true
created: 2024-12-06T06:58:21.117+01:00
modified: 2025-05-26T17:03:23.000+02:00
published: 2025-05-26T17:03:23.000+02:00
---

#awk/print #awk/nf

> [!info] Source
>
> - <https://unix.stackexchange.com/a/64674/482223>

```shell
echo "This is a test" | awk '{ print$(NF-2) }'
is
```
