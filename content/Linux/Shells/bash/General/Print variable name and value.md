---
publish: true
created: 2025-05-15T09:01:50.592+02:00
modified: 2025-05-26T15:25:11.200+02:00
published: 2025-05-26T15:25:11.200+02:00
cssclasses: ""
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