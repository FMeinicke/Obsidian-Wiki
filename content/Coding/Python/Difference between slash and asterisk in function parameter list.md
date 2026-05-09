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
