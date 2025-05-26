---
{"publish":true,"cssclasses":""}
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