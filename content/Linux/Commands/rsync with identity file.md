---
publish: true
created: 2025-05-15T09:01:49.639+02:00
modified: 2025-05-26T15:25:08.591+02:00
published: 2025-05-26T15:25:08.591+02:00
cssclasses: ""
---


#rsync/-e #rsync/--rsh

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/127355/482223>

- use the `--rsh=COMMAND`/`-e` flag
```shell
rsync -e "ssh -i ~/.ssh/id_rsa" ...
```
