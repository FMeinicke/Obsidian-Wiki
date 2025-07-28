---
{"publish":true,"created":"2025-05-15T09:01:46.794+02:00","modified":"2025-05-26T15:25:01.652+02:00","published":"2025-05-26T15:25:01.652+02:00","cssclasses":""}
---

#python/property/getter #python/property/setter

> [!info] See also
>
> - <https://gist.github.com/FMeinicke/701bf3942bb05d8e85e76703a783232a>

```python
from abc import ABC, abstractmethod

class MyABC(ABC):
  @property
  @abstractmethod
  def my_property(self) -> Any:
    raise NotImplementedError()

class MyDerived(MyABC):
  @MyABC.my_property.getter
  def my_property(self) -> Any:
    return ...

  # once this class has a property called `my_property`, we can also set a setter function for it
  @my_property.setter
  def my_property(self, val: Any) -> None:
    ...
```