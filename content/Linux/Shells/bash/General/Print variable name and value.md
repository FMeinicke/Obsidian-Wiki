---
publish: true
created: 2024-12-06T06:58:13.797+01:00
modified: 2025-05-26T17:02:37.000+02:00
published: 2025-05-26T17:02:37.000+02:00
---

#bash/echo #bash/expansion

> [!info] Source
>
> - <https://unix.stackexchange.com/a/397588/482223>

```shell
$ VAR="foo"
$ echo ${VAR@A}
VAR='foo'
$ export VAR
$ echo ${VAR@A}
declare -x VAR='foo'
```
