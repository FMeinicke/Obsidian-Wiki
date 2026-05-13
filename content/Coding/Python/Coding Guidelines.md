---
publish: true
created: 2025-05-15T09:01:46.513+02:00
modified: 2026-02-09T13:03:30.317+01:00
published: 2026-02-09T13:03:30.317+01:00
cssclasses: ""
---

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
- **Always use `raise Exception` instead of `raise Exception()`.**  
  When there are no arguments, no parentheses are required and according to [this SO answer](https://stackoverflow.com/a/16709222/12780516#:~:text=that%20said%2C%20even%20though%20the%20semantics%20are%20the%20same%2C%20the%20first%20form%20is%20microscopically%20faster), this should even be a bit faster than raising the exception instance.
    - Also see ruff's [unnecessary-paren-on-raise-exception (RSE102)](https://docs.astral.sh/ruff/rules/unnecessary-paren-on-raise-exception/#unnecessary-paren-on-raise-exception-rse102).
- **Use `tuple`s instead of `list`s for `Iterable` arguments**  
  Tuples are immutable, lists are mutable. If a function only requires some kind of iterable container, and you pass that container in-place (i.e., without assigning it to a variable), use a tuple.
    - E.g., `some_func((1, 2, 3,))` instead of `some_func([1, 2, 3])`.
- **Use the suffix *`Mixin`* for mixin classes.**  
  This is the recommended naming practice and indicates clearly that a class is a mixin and thus not to be used as a regular base class.
- **Add annotations whenever necessary (function parameters, return values, class member variable declarations) and use PEP 585 and PEP 604 syntax for type annotations.**  
- **Use a line length of 120 characters.**  
  The default 80 which has been established in most other languages seems to be a bit too small for most Python applications I've written so far. 120 using [ruff](https://docs.astral.sh/ruff/) with the default settings gives a very nice look 95% of the time, reducing the need to surround code with `# fmt: off` and `# fmt: on` comments to do manual formatting
- **Use [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html) for doc comments.**  
  See [[example.py]]:

- **Use `%s` formatting syntax as the preferred method for logging messages.**  
  This is the recommended way according to the logging module's documentation as this ensures that "Formatting of message arguments is deferred until it cannot be avoided." Using f-string syntax might have an extra cost as it will format the message even if it is not logged.
  f-strings may be used instead when they significantly increase readability, or are necessary for complex formatting (that can't be achieved using the older `%s` formatting) or embedded expressions.
  ```python
  # prefer
  logging.debug("some message %s: %d", var, 42)
  # over
  logging.debug(f"some message {var}: 42")
  ```
- **Use the `@override` decorator from the `typing` module to mark functions in subclasses that override base class functions.**  
  This ensures that the subclass method has the same signature as the base class method and can prevent subtle bugs when the base class method changes, for example.
- **Use the `@final` decorator from the `typing` module to mark functions and properties in base classes as "not to be overridden by subclasses".**  
  This prevents accidental overwriting of these methods/properties by subclasses.
- **Prefer relative imports when importing from the current directory/package at the top level.**  
  Do use `from . import ...` or `from .sibling.sibling import ...`. This reduces writing boilerplate package paths and makes it easier to distinguish imports of modules in the same package/directory from the ones outside the current package/directory.
- **Prefer absolute imports when importing from outside the current directory/package.**  
  Don't use `from .. import ...` or `from ...grandcousin import ...`. This is error-prone and makes it hard to trace the actual module that is being imported (especially for common modules like `util` or `const`).
- **Prefer absolute imports in all cases when importing inside a function or method.**  
  This avoids ambiguity and makes the import explicit and easier to debug.
