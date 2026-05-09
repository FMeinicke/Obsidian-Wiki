---
publish: true
created: 2024-12-06T06:58:25.823+01:00
modified: 2025-05-26T17:04:06.000+02:00
published: 2025-05-26T17:04:06.000+02:00
---

#git/reset/soft #git/restore/staged

> [!info] Source
>
> - <https://www.git-tower.com/learn/git/faq/undo-last-commit>

```shell
git reset --soft HEAD~             # keeps the files staged
git restore --staged <files...>    # unstages the files
git restore <files...>             # restores the files to before the commit
```
