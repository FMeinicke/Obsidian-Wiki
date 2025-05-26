---
publish: true
sorting-spec: |-
  find
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [`chmod` all files or directories recursively](Linux/Commands/find/`chmod` all files or directories recursively.md)
- [Find hardlinks](Linux/Commands/find/Find hardlinks.md)
- [Use `bash -c` in `-exec`](Linux/Commands/find/Use `bash -c` in `-exec`.md)

---



#find/exec #find/print0 #chmod #xargs

> [!info] Source
>
> - <https://superuser.com/a/91938>

To recursively give **directories** read & execute privileges:

```shell
find /path/to/base/dir -type d -exec chmod 755 {} +
```

To recursively give **files** read privileges:

```shell
find /path/to/base/dir -type f -exec chmod 644 {} +
```

Or, if there are many objects to process:

```shell
chmod 755 $(find /path/to/base/dir -type d)
chmod 644 $(find /path/to/base/dir -type f)
```

Or, to reduce `chmod` spawning:

```shell
find /path/to/base/dir -type d -print0 | (sudo) xargs -0 chmod 755
find /path/to/base/dir -type f -print0 | (sudo) xargs -0 chmod 644
```



#find/type #find/links

> [!info] Source
> 
> - <https://askubuntu.com/a/972244/1152691>

```shell
find -type f -links +1
```



#find/exec/bash

> [!info] Source(s)
> 
> - <https://stackoverflow.com/a/40149174/12780516>

```shell
sudo find /usr/lib -iname '*boost*.so.1.*' -exec bash -c 'sudo ln -s ${1##*/} ${1/%1.83.0/1.74.0}' _ {} \;
```

- this can also be used to execute multiple arguments within the bash command line

---

---

## Tagged mentions


