---
{"publish":true,"cssclasses":"hide_properties"}
---


- [Moving an object to a different thread](Coding/Qt/Moving an object to a different thread.md)
- [QMake](QMake)
    - [Check for ARM architecture](Coding/Qt/QMake/Check for ARM architecture.md)
    - [Literal dollar sign](Coding/Qt/QMake/Literal dollar sign.md)
    - [Proper quoting and path separators](Coding/Qt/QMake/Proper quoting and path separators.md)
    - [Use `lld`](Coding/Qt/QMake/Use `lld`.md)

---


#QObject/moveToThread #QThread

> [!info] Source
> 
> - <https://doc.qt.io/qt-6/qobject.html#moveToThread>

> [!important]
> 
> **An object can only be "pushed" to another thread (i.e., the current thread must be the same as the object's thread), it cannot be "pulled" from an arbitrary thread to the current thread!**



- [`Iterable` vs. `Sequence`](Coding/Python/`Iterable` vs. `Sequence`.md)
- [abstract property](Coding/Python/abstract property.md)
- [abstract static property](Coding/Python/abstract static property.md)
- [Access `dist-packages` when inside a venv](Coding/Python/Access `dist-packages` when inside a venv.md)
- [Check if type is built-in](Coding/Python/Check if type is built-in.md)
- [Coding Guidelines](Coding/Python/Coding Guidelines.md)
- [Difference between slash and asterisk in function parameter list](Coding/Python/Difference between slash and asterisk in function parameter list.md)
- [Dynamically add property to a class](Coding/Python/Dynamically add property to a class.md)
- [Find the path to actual installation directory for the Windows Store version](Coding/Python/Find the path to actual installation directory for the Windows Store version.md)
- [Function decorator that accepts optional keyword-argument](Coding/Python/Function decorator that accepts optional keyword-argument.md)
- [Get class of a generic class's `TypeVar`](Coding/Python/Get class of a generic class's `TypeVar`.md)
- [Get the number of parameters for a function](Coding/Python/Get the number of parameters for a function.md)
- [How to use `Q_ARG` and `Q_RETURN_ARG` with `QMetaObject.invokeMethod()` in PySide6](Coding/Python/How to use `Q_ARG` and `Q_RETURN_ARG` with `QMetaObject.invokeMethod\(\)` in PySide6.md)
- [Mock an `ImportError` with pytest](Coding/Python/Mock an `ImportError` with pytest.md)
- [Proper Ctrl+C behavior with PySide2](Coding/Python/Proper Ctrl+C behavior with PySide2.md)
- [stub generation](Coding/Python/stub generation.md)


#coding-guidelines/python

- **Prefer `type(self)` over `self.__class__`.**  
  They're functionally equivalent, however
    - it's clearer, less typing, and more consistent (you wouldn't do `[1, 2, 3].__len__()` rather than `len([1, 2, 3])`)  
      <https://stackoverflow.com/questions/10386166/python-self-class-vs-typeself#comment13391384_10386227>,
    - `__class__` could be middle-manned by defining `__getattribute__()`, where `type()` cannot  
      <https://stackoverflow.com/questions/10386166/python-self-class-vs-typeself#comment123576009_10386227>,
    - in general, you should avoid using dunder names when there's a built-in method that does that for you  
      <https://stackoverflow.com/a/44460803/12780516>.
- **Always use `raise Exception from err` in an `except` block.**  
  This makes it easier to trace the exception back to its root cause.
    - See ruff's [raise-without-from-inside-except (B904)](https://docs.astral.sh/ruff/rules/raise-without-from-inside-except/).
- **Use `tuple`s instead of `list`s for `Iterable` arguments**  
  Tuples are immutable, lists are mutable. If a function only requires some kind of iterable container, and you pass that container in-place (i.e., without assigning it to a variable), use a tuple.
    - E.g., `some_func((1, 2, 3,))` instead of `some_func([1, 2, 3])`.
- **Use the suffix *`Mixin`* for mixin classes.***  
  This is the recommended naming practice and indicates clearly that a class is a mixin and thus not to be used as a regular base class.
- **Add annotations whenever necessary (function parameters, return values, class member variable declarations) and use PEP 585 and PEP 604 syntax for type annotations.**  
- **Use a line length of 120 characters.**  
  The default 80 which has been established in most other languages seems to be a bit too small for most Python applications I've written so far. 120 using [ruff](https://docs.astral.sh/ruff/) with the default settings gives a very nice look 95% of the time, reducing the need to surround code with `# fmt: off` and `# fmt: on` comments to do manual formatting
- **Use [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html) for doc comments.**  
  See [[example.py]]:
  ```python
undefined
```
- **Use `%s` formatting syntax as the preferred method for logging messages.**  
  This is the recommended way according to the logging module's documentation as this ensures that "Formatting of message arguments is deferred until it cannot be avoided." Using f-string syntax might have an extra cost as it will format the message even if it is not logged.
  f-strings may be used instead when they significantly increase readability, or are necessary for complex formatting (that can't be achieved using the older `%s` formatting) or embedded expressions.
  ```python
  # prefer
  logging.debug("some message %s: %d", var, 42)
  # over
  logging.debug(f"some message {var}: 42")
  ```


---


#python/stub #pyi #stubgen

> [!info] Source
>
> - <https://mypy.readthedocs.io/en/stable/stubgen.html>

```shell
stubgen -m <module_name> --include-private -o <output_dir>
```


#qt #qt-for-python #pyside #pyside2

> [!info] Source
>
> - <https://stackoverflow.com/a/11705366/12780516>
> - <https://stackoverflow.com/a/4939113/12780516>

```python
import signal

from PySide2.QtCore import QCoreApplication, QEvent

class CoreApplication(QCoreApplication):
    """needed for proper Ctrl-C behavior (see: https://stackoverflow.com/a/11705366/12780516)"""
    def event(self, event: QEvent) -> bool:
        return super().event(event)

def main():
    handler = None

    def handle_sigint(*args):
        print("handle_sigint")
        global app
        if app is None:
            print("received SIGINT before app was initialized")
            return
        signal.signal(signal.SIGINT, handler)
        app.quit()

    handler = signal.signal(signal.SIGINT, handle_sigint)
    global app
    app = CoreApplication()
    app.startTimer(100)
    app.exec_()


if __name__ == "__main__":
    main()
    print("done")
```

- for PySide6 **on Windows only!**, the only solution that works is to create a custom `CoreApplication` class which overrides `event`, catches `KeyboardInterrupt` in there and then quits the application

```python
from PySide6.QtCore import QCoreApplication, QEvent

class CoreApplication(QCoreApplication):
    """needed for proper Ctrl-C behavior (see: https://stackoverflow.com/a/11705366/12780516)."""

    def event(self, event: QEvent) -> bool:  # noqa: D102
        try:
            return super().event(event)
        except KeyboardInterrupt:
            # NOTE: this only works in a terminal but not in VSCode's debugger
            self.quit()
            return True


def main() -> None:
    """
    Main application entry point.
    """

    if (qapp := QCoreApplication.instance()) is None:
        import sys

        qapp = CoreApplication(sys.argv)
    else:
        # need to use our custom CoreApplication class to handle KeyboardInterrupt
        qapp.__class__ = CoreApplication

    qapp.startTimer(100)

    qapp.exec()


if __name__ == "__main__":
    main()
```

> [!note]- Previous answer
>
> This did not work in combination with a Typer application and I could later not even get this to work on its own in a simple test script.
>
> ```python
> if __name__ == "__main__":
>     class CoreApplication(QCoreApplication):
>         def event(self, event: QEvent) -> bool:
>             return super().event(event)
> 
>     app = CoreApplication([])
> 
>     signal.signal(signal.SIGINT, lambda *a: app.exit())
>     app.startTimer(100)
> 
>     # ...
> 
>     sys.exit(app.exec_())
> ```
>
> - `QCoreApplication.event` has to be re-implemented for some reason otherwise the timer will not work as intended
> - without re-implementation the same can be achieved by using
>
>   ```python
>     timer = QTimer()
>     timer.start(100)  # Let the interpreter run every 100 ms.
>     timer.timeout.connect(lambda: None)
>   ```
>
>   in place of
>
>   ```python
>   app.startTimer(100)
>   ```


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


#python/property

> [!info] Source
>
> - <https://stackoverflow.com/a/1355444/12780516>

```python
class Foo:
    ...

Foo.dynamic_prop = property(lambda s: "getter", lambda s, v: "setter")
```

- also works if there are already instances of that class --> those will have the dynamic property, as well


#pyside6 #Q_ARG #Q_RETURN_ARG #QMetaObject/invokeMethod

> [!info] Source
> 
> - lots of trail and error
> - <https://codereview.qt-project.org/c/pyside/pyside-setup/+/408145/18/sources/pyside6/tests/QtCore/qmetaobject_test.py>

- an (over-complicated) example that creates an object in the thread of the `RemoteControl` object

```python
class RemoteControl(QObject):

    __thread: QThread

    def create_object_in_thread(self, object_type: type[_RemoteObjectT], *args, **kwargs) -> _RemoteObjectT:
        """
        Create a RemoteObject derived object in the thread where the RemoteControl object lives.

        Parameters
        ----------
        object_type : type[_RemoteObjectT]
            The type of the object to create
        args : Any
            Positional arguments for the object constructor
        kwargs : Any
            Keyword arguments for the object constructor

        Returns
        -------
        _RemoteObjectT
            The created object
        """

        return self._create_object_in_thread(object_type, args, kwargs)

    @Slot("QVariant", "QVariantList", "QVariantMap", result=QObject)  # type: ignore[arg-type]
    def _create_object_in_thread(self, object_type: type[QObject], args, kwargs) -> QObject:
        """
        Helper function to allow calling `create_object_in_thread()` in another thread via `QMetaObject.invokeMethod()`
        and correctly map `args` and `kwargs` to the QMetaType system and back.
        """

        if QThread.currentThread() != self.__thread:
            obj: QObject = QMetaObject.invokeMethod(
                self,
                "_create_object_in_thread",  # type: ignore[arg-type]
                Qt.ConnectionType.BlockingQueuedConnection,
                Q_RETURN_ARG(QObject),
                Q_ARG("QVariant", object_type),
                Q_ARG("QVariantList", args),
                Q_ARG("QVariantMap", kwargs),
            )
            return obj

        return object_type(*args, **kwargs)
```

- this is, by the way, way too complicated and can be solved by a much simpler implementation

```python
class RemoteControl(QObject):

    __thread: QThread

    def create_object_in_thread(self, object_type: type[_RemoteObjectT], *args, **kwargs) -> _RemoteObjectT:
        """
        Create a RemoteObject derived object in the thread where the RemoteControl object lives.

        Parameters
        ----------
        object_type : type[_RemoteObjectT]
            The type of the object to create
        args : Any
            Positional arguments for the object constructor
        kwargs : Any
            Keyword arguments for the object constructor

        Returns
        -------
        _RemoteObjectT
            The created object
        """

        obj = object_type(*args, **kwargs)
        obj.moveToThread(self.__thread)
        return obj
```


#python/venv #python/dist-packages #python/site-packages

> [!info] Source
> 
> - <https://stackoverflow.com/a/47842938/12780516>

- by default, python will only have access to the `site-packages` directly installed inside a venv
- if we want to access the packages from the (Linux) system's `dist-packages` that were installed using the system's package manager, there are multiple possible ways
    1. set `PYTHONPATH` to include `/usr/lib/python<VERSION>/dist-packages`
       this has the drawback that now the `dist-packages` take precedence over the `site-packages` from the venv, thus if we have the same package installed in the venv but with a different (usually more recent) version than in the `dist-packages`, python will use the one from the `dist-packages`, which is usually not what we want
    2. create a `.pth` file in the venv's `site-packages` folder that points to the system's `dist-packages`
       this has the advantage, that the venv's packages will be used first and only if python cannot find a package in the venv, it will go looking into the system's `dist-packages`

    ```shell
    echo "/usr/lib/python<VERSION>/dist-packages" > .venv/lib/python<VERSION>/site-packages/dist-packages.pth
    ```

    (the `<VERSION>` has to match, of course, so for Python 3.10, for example, this would read `python3.10` in both cases)


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

---
publish: true
title: Difference between slash (`/`) and asterisk (`*`) in function parameter list
cssclasses:
  - hide_properties
---
#python/slash #python/asterisk #python/parameters #python/functions

> [!info] Source
> 
> - <https://realpython.com/python-asterisk-and-slash-special-parameters/>

- the **slash (`/`)** separates **positional-only** arguments from **positional or keyword** arguments
- the **asterisk (`*`)** separates **positional or keyword** arguments from **keyword-only** arguments
- if **both** occur in a parameter list, the **slash (`/`)** must come **before** the **asterisk (`*`)**

```python
def slash_usage(positional_only, /, either):
    print(positional_only, either)

def asterisk_usage(either, *, keyword_only):
    print(either, keyword_only)

def both_usage(positional_only, /, either, *, keyword_only):
    print(positional_only, either, keyword_only)
```

- using slash (`/`) and asterisk (`*`) directly after each other, forces everything left of the slash to be passed by position-only and everything to the right to be passed by keyword-only

```python
def both_usage(positional_only, /, *, keyword_only):
    print(positional_only, keyword_only)
```


#python/decorator #python/wraps #python/overload

> [!info] Source
> 
> - self, with help from GitHub Copilot
> - inspired by `@dataclass`'s handling of optional keyword arguments (albeit being to decorate classes rather than functions)

```python
from __future__ import annotations

from functools import wraps
from typing import overload


@overload
def func_decorator_with_and_without_args(func): ...


@overload
def func_decorator_with_and_without_args(*, dkwarg="default_kwarg"): ...


def func_decorator_with_and_without_args(*dargs, dkwarg="default_kwarg"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(
                f"func_decorator_with_and_without_args: Calling {func.__name__} with args: {args}, kwargs: {kwargs}, "
                f"decorator dkwarg: {dkwarg}"
            )
            return func(*args, **kwargs)

        return wrapper

    print(f"decorator dargs: {dargs}, decorator dkwarg: {dkwarg}")

    if len(dargs) > 1:
        raise ValueError("Only one positional argument is allowed (the function to decorate)")

    # see if we're being called as @decorator or @decorator()
    if len(dargs) == 0:
        # we're called with parentheses as @decorator(kwargs...)
        return decorator

    # we're called as @decorator without parentheses
    func = dargs[0]
    if not callable(func):
        raise TypeError("The function to decorate must be a callable")
    return decorator(func)

# valid usage -----------------------------------------------------------

@func_decorator_with_and_without_args
def func(*args, **kwargs):
    print(f"func args: {args}, kwargs: {kwargs}")

@func_decorator_with_and_without_args(dkwarg="dkwarg")
def func_with_args(*args, **kwargs):
    print(f"func_with_args args: {args}, kwargs: {kwargs}")

# invalid usage ---------------------------------------------------------

@func_decorator_with_and_without_args()
def func_with_empty_parens(*args, **kwargs):
    print(f"func_with_empty_parens args: {args}, kwargs: {kwargs}")

@func_decorator_with_and_without_args("darg")
def func_with_single_arg_invalid(*args, **kwargs):
    print(f"func_with_single_arg_invalid args: {args}, kwargs: {kwargs}")

@func_decorator_with_and_without_args("darg1", "darg2")
def func_with_args_invalid(*args, **kwargs):
    print(f"func_with_args_invalid args: {args}, kwargs: {kwargs}")

@func_decorator_with_and_without_args(dkwarg="dkwarg", dkwarg2="dkwarg2")
def func_with_multiple_kwargs_invalid(*args, **kwargs):
    print(f"func_with_multiple_kwargs_invalid args: {args}, kwargs: {kwargs}")
```


#python/windows

> [!info] Source
> 
> - trial and error

```python
>>> import os
>>> os.__file__
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib\\os.py'
```


#python/type/built-in #python/builtins

> [!info] Source
> 
> - GitHub Copilot
> - <https://stackoverflow.com/a/17795199/12780516>

```python
var: int = 42
type(var).__module__ == "builtins"
```


#pytest/monkeypatch #python/builtins #python/importlib

> [!info] Source
> 
> - <https://stackoverflow.com/a/2481588/12780516>

- use the (already defined) pytest `monkeypatch` fixture to temporarily modify the state of the `builtins` module and the `sys.modules` `dict`
- define a custom import function that raises `ImportError` when a certain module (in this case named `labbcan`) is requested to be imported
- force a reload of the module that imports the module that should be mocked to be not existent (in this case `cetoni_qtro_models.linear_scaling`)  
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



---

## Tagged mentions




---

## Tagged mentions


