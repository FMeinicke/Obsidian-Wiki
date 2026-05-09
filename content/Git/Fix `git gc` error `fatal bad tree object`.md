---
publish: true
created: 2024-12-06T06:58:16.864+01:00
modified: 2025-05-26T17:02:55.000+02:00
published: 2025-05-26T17:02:55.000+02:00
---

#git/fetch/--refetch #git/gc/--aggressive

> [!info] Source
>
> - <https://stackoverflow.com/a/74286404/12780516>

- this error might happen during a `git fetch`:

```shell
git fetch
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
warning: The last gc run reported the following. Please correct the root cause
and remove .git/gc.log
Automatic cleanup will not be performed until the file is removed.

fatal: bad tree object 9213e6d7ad31bde664dd103745302c3750cbecbd
fatal: failed to run repack
```

- it can be resolved by running

```shell
git fetch --refetch
git gc --aggressive
```
