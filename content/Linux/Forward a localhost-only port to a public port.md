---
{"publish":true,"cssclasses":""}
---


#socat/tcp-listen

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/187038/482223>

- use `socat` to create a tunnel from the localhost-only port to another port that is then publicly accessible

```shell
socat tcp-listen:<public port>,reuseaddr,fork tcp:localhost:<localhost-only port>
```
