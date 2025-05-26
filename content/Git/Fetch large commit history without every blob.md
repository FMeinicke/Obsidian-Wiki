---
{"publish":true,"cssclasses":""}
---

#git/--filter #git/blob

> [!info] Source
> 
> - <https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/#user-content-partial-clone>

- use `--filter=blob:none` to only download the commits and trees

```shell
git clone --filter=blob:none <url>
# or
git fetch --filter=blob:none [options...]
```

- only when you then do a checkout of a certain commit, git will download the corresponding blobs for that commit
