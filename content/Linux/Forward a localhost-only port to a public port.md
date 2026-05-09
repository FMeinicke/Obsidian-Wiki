---
publish: true
created: 2024-12-06T06:58:15.444+01:00
modified: 2025-05-26T17:02:44.000+02:00
published: 2025-05-26T17:02:44.000+02:00
---

#socat/tcp-listen

> [!info] Source
>
> - <https://unix.stackexchange.com/a/187038/482223>

- use `socat` to create a tunnel from the localhost-only port to another port that is then publicly accessible

```shell
socat tcp-listen:<public port>,reuseaddr,fork tcp:localhost:<localhost-only port>
```
