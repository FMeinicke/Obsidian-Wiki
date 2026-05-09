---
publish: true
created: 2024-12-06T06:58:16.337+01:00
modified: 2025-05-26T17:02:48.000+02:00
published: 2025-05-26T17:02:48.000+02:00
---

#linux/cp #cp/remove-destination #linux/ln #ln/f #linux/readlink

> [!info] Source
>
> - <https://stackoverflow.com/a/75263788/12780516>
> - <https://stackoverflow.com/a/13396140/12780516>

```shell
ln -f $(readlink bar.pdf) bar.pdf                    # makes it a hardlink to the same file
cp --remove-destination $(readlink bar.pdf) bar.pdf  # makes it a completely separate regular file
```
