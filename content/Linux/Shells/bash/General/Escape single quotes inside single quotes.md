---
publish: true
created: 2024-12-06T06:58:11.094+01:00
modified: 2025-05-26T17:02:23.000+02:00
published: 2025-05-26T17:02:23.000+02:00
---

#bash/echo #bash/escaping #bash/quotes

> [!info] Source
>
> - <https://stackoverflow.com/a/1250279/12780516>

- use double quotes to "escape" one single quote after ending the single quoted string and before starting the next part of the single quoted string

```shell
$ echo 'this is a single quote '"'"' inside a single quoted string'
this is a single quote ' inside a single quoted string
```

---
