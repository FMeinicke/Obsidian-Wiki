---
{"publish":true,"created":"2025-05-15T09:01:49.388+02:00","modified":"2025-05-26T15:25:08.137+02:00","published":"2025-05-26T15:25:08.137+02:00","cssclasses":""}
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