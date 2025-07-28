---
{"publish":true,"title":"Set branch to certain/current commit without checking out that branch","created":"2025-05-15T09:01:47.982+02:00","modified":"2025-06-04T11:18:53.866+02:00","published":"2025-06-04T11:18:53.866+02:00","cssclasses":""}
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