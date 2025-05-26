---
{"publish":true,"cssclasses":""}
---


#find/exec/bash

> [!info] Source(s)
> 
> - <https://stackoverflow.com/a/40149174/12780516>

```shell
sudo find /usr/lib -iname '*boost*.so.1.*' -exec bash -c 'sudo ln -s ${1##*/} ${1/%1.83.0/1.74.0}' _ {} \;
```

- this can also be used to execute multiple arguments within the bash command line

---