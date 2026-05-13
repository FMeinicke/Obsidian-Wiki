---
publish: true
created: 2025-05-15T09:01:47.388+02:00
modified: 2025-05-26T15:25:05.528+02:00
published: 2025-05-26T15:25:05.528+02:00
cssclasses: ""
---

#gpg/export

> [!info] Source
>
>

```shell
gpg -a --export KEYID > <user>.<name>.gpg.public
gpg -a --export-secret-keys KEYID > <user>.<name>.gpg.private
```