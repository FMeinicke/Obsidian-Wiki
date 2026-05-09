---
publish: true
created: 2025-03-08T16:46:36.971+01:00
modified: 2025-05-26T17:02:28.000+02:00
published: 2025-05-26T17:02:28.000+02:00
---

#ls/-al #bash/for #ls/-1 #cat/-v #line-endings #line-endings/crlf #line-endings/lf #tr/-d

> [!info] Source
>
> - <https://stackoverflow.com/a/77198331/12780516>

- ensure that the hooks are executable and contain Linux line endings (LF instead of CRLF)

```shell
ls -al .git/hooks/
for f in $(ls -1 .git/hooks/* | grep -v '.sample'); do cat -v ${f}; done
```

(look for `^M` sequences in the `cat` output -> this means that the file has Windows CRLF line endings)

- to convert all hooks

```shell
for f in $(ls -1 .git/hooks/* | grep -v '.sample'); do cat -v ${f} | tr -d '\r' > ${f}.tmp && mv ${f}.tmp ${f}; done
```

(see [[ls with path]])
