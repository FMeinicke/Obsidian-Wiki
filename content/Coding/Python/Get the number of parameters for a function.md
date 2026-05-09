---
publish: true
created: 2025-03-08T16:46:36.998+01:00
modified: 2025-05-26T17:02:33.000+02:00
published: 2025-05-26T17:02:33.000+02:00
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
