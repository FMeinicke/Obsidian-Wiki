---
publish: true
created: 2025-03-08T16:46:39.155+01:00
modified: 2025-05-26T17:03:31.000+02:00
published: 2025-05-26T17:03:31.000+02:00
---

#qmake/dollar

> [!info] Source
>
> - <https://forum.qt.io/post/426213>

- use an escaped dollar sign **twice!**

```qmake
my_custom_target.command = $$QMAKE_MOVE \$\$file \$\$other_file
```

will result in the shell command `mv -f $filw $other_file`

(I think the double dollar sign is necessary to escape the first dollar sign in the Makefile, and the backslashes just escape the dollar signs for qmake so that they end up as literal dollar signs in the Makefile)
