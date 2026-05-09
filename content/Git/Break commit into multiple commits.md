---
publish: true
created: 2024-12-06T06:58:20.547+01:00
modified: 2025-05-26T17:03:18.000+02:00
published: 2025-05-26T17:03:18.000+02:00
---

#git/commit #git/reset #git/rebase/interactive #git/rebase/edit

> [!info] Source
>
> - <https://stackoverflow.com/a/6217314/12780516>

### Split the most recent commit

```shell
git reset HEAD~
```

- then commit the pieces individually as usual

### Split an older commit (during a rebase)

```shell
git rebase -i <commit-ish>
```

- in the rebase editor select `edit` for the commit to be split; save and close
- you should now be at the correct point in the commit history, so again

```shell
git reset HEAD~
```

- and again, commit the pieces individually as usual
