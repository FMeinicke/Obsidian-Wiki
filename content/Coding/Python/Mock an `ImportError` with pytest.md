---
publish: true
created: 2025-03-08T16:46:38.265+01:00
modified: 2025-05-26T17:02:53.000+02:00
published: 2025-05-26T17:02:53.000+02:00
---

#pytest/monkeypatch #python/builtins #python/importlib

> [!info] Source
>
> - <https://stackoverflow.com/a/2481588/12780516>

- use the (already defined) pytest `monkeypatch` fixture to temporarily modify the state of the `builtins` module and the `sys.modules` `dict`
- define a custom import function that raises `ImportError` when a certain module (in this case named `labbcan`) is requested to be imported
- force a reload of the module that imports the module that should be mocked to be not existent (in this case `cetoni_qtro_models.linear_scaling`)\
  -> this reload will in turn try to import `labbcan` again which will fail with an `ImportError`

```python
import builtins
import importlib
import sys
from collections.abc import Mapping, Sequence
from types import ModuleType

import pytest

realimport = builtins.__import__


def no_labbcan_import(
    name: str,
    globals: Mapping[str, object] | None = None,  # noqa: A002
    locals: Mapping[str, object] | None = None,  # noqa: A002
    fromlist: Sequence[str] = (),
    level: int = 0,
) -> ModuleType:
    if name.startswith("labbcan"):
        raise ImportError
    return realimport(name, globals, locals, fromlist, level)


def test_import_error(monkeypatch: pytest.MonkeyPatch) -> None:
    with monkeypatch.context() as m:
        m.setattr(builtins, "__import__", no_labbcan_import)
        m.delitem(sys.modules, "cetoni_qtro.models.linear_scaling")

        importlib.reload(cetoni_qtro.models)
        from cetoni_qtro.models.linear_scaling import LinearScaling
        # test what ever you like without labbcan being imported if the reloaded module already
        # handles the `ImportError` gracefully
        
        # or
        with pytest.raises(ImportError):
            importlib.reload(cetoni_qtro.models)
            from cetoni_qtro.models.linear_scaling import LinearScaling
```
