---
publish: true
created: 2025-05-15T09:01:50.233+02:00
modified: 2025-05-26T15:25:10.200+02:00
published: 2025-05-26T15:25:10.200+02:00
cssclasses: ""
---


#socat/tcp-listen

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/187038/482223>

- use `socat` to create a tunnel from the localhost-only port to another port that is then publicly accessible

```shell
socat tcp-listen:<public port>,reuseaddr,fork tcp:localhost:<localhost-only port>
```
