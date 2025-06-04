---
{"publish":true,"title":"Set branch to certain/current commit without checking out that branch","cssclasses":""}
---

#git/branch/force

> [!info] Source
> 
> - <https://stackoverflow.com/a/5471197/12780516>

```shell
git branch --force <branch-name> [<new-tip-commit>]
```

- without `<new-tip-commit>` this defaults to setting the branch to the current commit
- `<new-tip-commit>` can also be another branch name (e.g., `main`, `origin/main`)