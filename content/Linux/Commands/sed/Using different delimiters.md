---
{"publish":true,"cssclasses":""}
---


#sed

> [!info] Source
>
> - <https://backreference.org/2010/02/20/using-different-delimiters-in-sed/index.html>

```shell
#do this (ugly)...
sed '/\/a\/b\/c\//{do something;}'
# ...or these (better)
sed '\#/a/b/c/#{do something;}'
sed '\_/a/b/c/_{do something;}'
sed '\%/a/b/c/%{do something;}'
#etc.
```
