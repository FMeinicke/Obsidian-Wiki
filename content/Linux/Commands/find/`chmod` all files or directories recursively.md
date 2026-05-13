---
publish: true
created: 2025-05-15T09:01:49.404+02:00
modified: 2025-05-26T15:25:08.184+02:00
published: 2025-05-26T15:25:08.184+02:00
cssclasses: ""
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