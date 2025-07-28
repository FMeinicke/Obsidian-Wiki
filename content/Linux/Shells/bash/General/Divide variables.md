---
{"publish":true,"created":"2025-05-15T09:01:50.498+02:00","modified":"2025-05-26T15:25:10.825+02:00","published":"2025-05-26T15:25:10.825+02:00","cssclasses":""}
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
