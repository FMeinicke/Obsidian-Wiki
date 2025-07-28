---
{"publish":true,"created":"2025-05-15T09:01:48.029+02:00","modified":"2025-05-26T15:25:05.152+02:00","published":"2025-05-26T15:25:05.152+02:00","cssclasses":""}
---

#git/submodule/foreach #linux/sh #linux/bash #bash

> [!info] Source
> 
> - <https://stackoverflow.com/a/65086817/12780516>

- git uses `/bin/sh`, so we simply need to link this to our desired shell (e.g., `bash`)

```shell
sudo ln -sf bash /bin/sh
```