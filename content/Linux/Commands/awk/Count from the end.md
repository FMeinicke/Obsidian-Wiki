---
{"publish":true,"cssclasses":""}
---


#awk/print #awk/nf

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/64674/482223>

```shell
echo "This is a test" | awk '{ print$(NF-2) }'
is
```