---
{"publish":true,"created":"2025-05-15T09:01:48.451+02:00","modified":"2025-05-26T15:25:05.043+02:00","published":"2025-05-26T15:25:05.043+02:00","cssclasses":""}
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