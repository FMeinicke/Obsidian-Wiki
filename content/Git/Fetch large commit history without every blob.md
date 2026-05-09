---
publish: true
created: 2024-12-06T06:58:16.350+01:00
modified: 2025-05-26T17:02:48.000+02:00
published: 2025-05-26T17:02:48.000+02:00
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
