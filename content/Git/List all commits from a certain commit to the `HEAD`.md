---
publish: true
created: 2025-05-15T09:01:47.810+02:00
modified: 2025-05-26T15:25:04.277+02:00
published: 2025-05-26T15:25:04.277+02:00
cssclasses: ""
---

#git/log/format #git/log/reverse

> [!info] Source(s)
> 
> - shell history

```shell
git log --format=%H --reverse <commit hash>..HEAD > commits.txt
```