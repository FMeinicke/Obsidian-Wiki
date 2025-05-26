---
{"publish":true,"cssclasses":""}
---


#python/inspect/signature

> [!info] Source
> 
> - <https://stackoverflow.com/a/41188411/12780516>

```python
from inspect import signature

def some_func(a, b, c) -> None:
    pass

params = signature(some_func).parameters
num_params = len(params)
```
