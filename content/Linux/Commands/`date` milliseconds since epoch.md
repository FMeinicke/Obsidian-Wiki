---
publish: true
created: 2025-03-12T16:54:06.846+01:00
modified: 2025-05-26T17:02:57.000+02:00
published: 2025-05-26T17:02:57.000+02:00
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
