---
{"publish":true,"cssclasses":""}
---

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