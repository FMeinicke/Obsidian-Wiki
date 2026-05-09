---
publish: true
created: 2024-12-06T06:58:17.274+01:00
modified: 2025-05-26T17:02:59.000+02:00
published: 2025-05-26T17:02:59.000+02:00
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
