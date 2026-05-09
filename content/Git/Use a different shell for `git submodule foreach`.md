---
publish: true
created: 2024-12-06T06:58:15.054+01:00
modified: 2025-05-26T17:02:42.000+02:00
published: 2025-05-26T17:02:42.000+02:00
---

#git/submodule/foreach #linux/sh #linux/bash #bash

> [!info] Source
>
> - <https://stackoverflow.com/a/65086817/12780516>

- git uses `/bin/sh`, so we simply need to link this to our desired shell (e.g., `bash`)

```shell
sudo ln -sf bash /bin/sh
```
