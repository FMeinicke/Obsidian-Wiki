---
publish: true
created: 2025-03-12T16:54:06.852+01:00
modified: 2025-05-26T17:03:08.000+02:00
published: 2025-05-26T17:03:08.000+02:00
---

#bash/arithmethic-expression #linux/bc

> [!info] Source
>
> - <https://stackoverflow.com/a/30398152/12780516>

- using an arithmetic expression (`$(( $a / $b ))`) only gives an integer result
- use `bc` for proper floating point math

```shell
a=100
b=42
echo $a / $b = $(bc <<<"scale=2; $a / $b")
```
