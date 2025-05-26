---
{"publish":true,"cssclasses":""}
---

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