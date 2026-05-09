---
publish: true
created: 2025-02-08T16:12:43.740+01:00
modified: 2025-05-26T17:03:16.000+02:00
published: 2025-05-26T17:03:16.000+02:00
---

#rsync/-e #rsync/--rsh

> [!info] Source
>
> - <https://unix.stackexchange.com/a/127355/482223>

- use the `--rsh=COMMAND`/`-e` flag

```shell
rsync -e "ssh -i ~/.ssh/id_rsa" ...
```
