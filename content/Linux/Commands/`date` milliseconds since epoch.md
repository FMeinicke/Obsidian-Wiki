---
{"publish":true,"cssclasses":""}
---


#date

> [!info] Source
> 
> - <https://serverfault.com/a/588705/600279>

- use `%N` to get the nanoseconds or `%3N` to truncate to milliseconds
```console
$ date +%s%N
1741787785964178320
$date +%s%3N
1741787794337
```
