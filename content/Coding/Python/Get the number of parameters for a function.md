---
publish: true
created: 2025-05-15T09:01:46.654+02:00
modified: 2025-05-26T15:25:02.214+02:00
published: 2025-05-26T15:25:02.214+02:00
cssclasses: ""
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
