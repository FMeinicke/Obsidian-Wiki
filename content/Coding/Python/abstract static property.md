---
publish: true
created: 2025-03-08T16:46:38.861+01:00
modified: 2025-05-26T17:03:20.000+02:00
published: 2025-05-26T17:03:20.000+02:00
---

#python/abc #python/property #python/staticmethod

> [!info] Source
>
> - <https://stackoverflow.com/a/64397790>

- the goal is to have an abstract base class which defines a property that all subclasses must provide
- this property is not dependent on the state of individual class instances, so it should be a static property
- the naive approach using a triple decorated function does not work

```python
from abc import ABC, abstractmethod

class Base(ABC):
    @property
    @staticmethod
    @abstractmethod
    def abstract_static_property():
        print("Base.abstract_static_property")
        raise NotImplementedError()
```

- instead, utilizing `__init_subclass__` in the abstract base class, we can emulate the behavior of such an abstract static property

```python
from abc import ABC, abstractmethod

class Base(ABC):
    abstract_static_property: T # either specify type or default value

    @classmethod
    def __init_subclass__(cls):
        if not any("abstract_static_property" in base.__dict__ for base in cls.__mro__ if base is not Base):
            raise NotImplementedError(
                f"Attribute 'abstract_static_property' has not been overwritten in class '{cls.__name__}'"
            )
```
