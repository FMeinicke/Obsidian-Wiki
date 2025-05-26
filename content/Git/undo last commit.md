---
{"publish":true,"cssclasses":""}
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