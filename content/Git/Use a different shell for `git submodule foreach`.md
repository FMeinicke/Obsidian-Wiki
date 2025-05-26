---
{"publish":true,"cssclasses":""}
---

#git/submodule/foreach #linux/sh #linux/bash #bash

> [!info] Source
> 
> - <https://stackoverflow.com/a/65086817/12780516>

- git uses `/bin/sh`, so we simply need to link this to our desired shell (e.g., `bash`)

```shell
sudo ln -sf bash /bin/sh
```