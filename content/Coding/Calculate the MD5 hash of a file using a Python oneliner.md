---
publish: true
created: 2026-05-09T11:02:58.496+02:00
modified: 2026-05-09T11:02:58.823+02:00
published: 2026-05-09T11:02:58.823+02:00
---

#hash/md5 #python/hashlib/md5

> [!info] Source
>
> - <https://stackoverflow.com/a/16876405/>
> - <https://gist.github.com/FMeinicke/a312e3069a573428afcdec92eee76ee0>

```console
$ python -c "import sys, hashlib; from pathlib import Path; print(f'{sys.argv[1]}: {hashlib.md5(Path(sys.argv[1]).read_bytes()).hexdigest()}')" /path/to/file
b8bbb321fb1d6834e5335b74e7222d08
```
