---
{"publish":true,"created":"2025-05-15T09:01:47.576+02:00","modified":"2025-05-26T15:25:03.574+02:00","published":"2025-05-26T15:25:03.574+02:00","cssclasses":""}
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