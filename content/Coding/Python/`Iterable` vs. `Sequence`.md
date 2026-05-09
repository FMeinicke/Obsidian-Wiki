---
publish: true
created: 2025-03-08T16:46:38.798+01:00
modified: 2025-05-26T17:03:16.000+02:00
published: 2025-05-26T17:03:16.000+02:00
---

#python/iterable #python/sequence #python/typing #python/collections/abc

> [!info] Source
>
> - Python stdlib code (`_collections_abc.py`)

- `Iterable` is more general
  - supports only `__iter__()`
- `Sequence` inherits `Iterable` (indirectly via `Collection`)
  - is in addition `Reversible` (supports `__reversed__`)
  - `Collection` inherits `Sized`, `Iterable` and `Container`
    - supports `__len__()` (from `Sized`)
    - supports `__iter__()` (from `Iterable`)
    - supports `__contains__()` (from `Container`)
  - `tuple` and `str` are two examples of concrete subclasses of `Sequence`
