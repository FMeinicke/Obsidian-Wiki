---
publish: true
created: 2024-12-06T06:58:11.744+01:00
modified: 2025-05-26T17:02:26.000+02:00
published: 2025-05-26T17:02:26.000+02:00
---

#threads #open-files #ps #lsof #printf

> [!info] Source

```bash
search_proc="<PROC>"; while true; do t=$(ps -fLu pi | grep $search_proc$ | wc -l); t2=$(ps -eLf | wc -l); f=$(lsof | wc -l); printf '\b%.0s' {1..100}; printf "$search_proc$: $t, all: $t2; files: $f"; printf '%.0s' {1..100}; printf '\b%.0s' {1..100}; sleep 0.5; done
```
