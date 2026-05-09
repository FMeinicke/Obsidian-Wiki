---
publish: true
created: 2025-03-08T16:46:37.591+01:00
modified: 2025-05-26T17:02:39.000+02:00
published: 2025-05-26T17:02:39.000+02:00
---

#python/generic #python/typevar

> [!info] Source
>
> - <https://discuss.python.org/t/inside-a-generic-class-how-to-get-the-class-of-type-variable/20792>
> - <https://stackoverflow.com/a/50101934/12780516>
> - <https://github.com/python/cpython/blob/374abded070b861cc389d509937344073193c36a/Lib/types.py#L169>

```python
from typing import Generic, TypeVar

_T = TypeVar("_T")

class MyGenericClass(Generic[_T]):
    def __init__(self) -> None:
        TType: type[_T] = type(self).__orig_bases__[0].__args__[0]
        t = TType(...)

        # the naive approach of just using _T does not work, because it's just a typing annotation
        t = _T(...)  # raises `TypeError: 'TypeVar' object is not callable`
```

- as an alternative we can use `get_original_bases()` from the `typing` module (only available from Python 3.12; use `typing_extensions` for earlier versions instead) in combination with `get_args()` for a more idiomatic version

```python
from typing import get_args, get_original_bases

# ...
TType: type[_T] = get_args(get_original_bases(type(self)))
```

- note that this might not work in all cases because `get_original_bases()` uses `cls.__dict__.get("__orig_bases__", cls.__bases__)` internally, which is not functionally equivalent (at least in Python 3.10)
- this can be mitigated by a custom implementation of `get_original_bases()`

```python
from typing import Iterable

def get_original_bases(cls: type, /) -> Iterable[type]:
    """
    Return the class's "original" bases, similar to `typing.get_original_bases()` for Python 3.12+, but not using
    `__orig_bases__` from the class's `__dict__` since this seems to not always be available that way
    (`cls.__orig_bases__` is, though).

    Parameters
    ----------
    cls : type
        The class to get the original bases for

    Returns
    -------
    Iterable[type]
        The original bases of the class
    """

    return getattr(cls, "__orig_bases__", cls.__bases__)

```
