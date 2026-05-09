---
publish: true
created: 2025-03-08T16:46:37.725+01:00
modified: 2025-05-26T17:02:48.000+02:00
published: 2025-05-26T17:02:48.000+02:00
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
