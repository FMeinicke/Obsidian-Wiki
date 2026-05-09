---
publish: true
created: 2025-01-18T15:02:46.700+01:00
modified: 2025-05-26T17:03:21.000+02:00
published: 2025-05-26T17:03:21.000+02:00
---

#git/stash/apply #git/gitk #git/fsck #awk #pwsh/select-string #pwsh/foreach

> [!info] Source
>
> - <https://stackoverflow.com/a/91795/12780516>

- to find the dropped stash / all unreferenced commits ever

```shell
gitk --all $( git fsck --no-reflog | awk '/dangling commit/ {print $NF}' )
```

- or on Windows

```powershell
gitk --all $( git fsck --no-reflog | select-string 'dangling commit' | foreach { $_.ToString().Split(" ")[-1] } )
```

- then look for _WIP on somebranch_ or _autostash_ commit messages
- once found, note the commit hash
- to apply the stash run

```shell
git stash apply $stash_hash
```
