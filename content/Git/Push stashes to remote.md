---
{"publish":true,"cssclasses":""}
---

#git/stash #git/push #git/refs #git/fetch #git/rstash

> [!info] Source
> 
> - <https://stackoverflow.com/a/61356308/12780516>
> - <https://github.com/501st-alpha1/git-rstash>

- TL;DR: use `git-rstash` from [here](https://github.com/501st-alpha1/git-rstash)
    - stashes are pushed as commits to `refs/stashes/`
    - when `fetch`ing the local `refs/stashes/` will be populated and `import`ing a stash (or all stashes) converts the commits to stashes using `git stash --store`

```console
git rstash push-all                        # pushes all stashes
git rstash push 0                          # pushes stash 0
git rstash fetch && git rstash import-all  # fetches all stashes and populates the local stash with them
```
