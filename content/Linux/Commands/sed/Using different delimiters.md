---
publish: true
created: 2025-05-15T09:01:49.701+02:00
modified: 2025-05-26T15:25:08.778+02:00
published: 2025-05-26T15:25:08.778+02:00
cssclasses: ""
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
