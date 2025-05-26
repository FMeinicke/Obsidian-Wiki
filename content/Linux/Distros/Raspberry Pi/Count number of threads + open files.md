---
{"publish":true,"cssclasses":""}
---


#threads #open-files #ps #lsof #printf

> [!info] Source
>
>

```bash
search_proc="<PROC>"; while true; do t=$(ps -fLu pi | grep $search_proc$ | wc -l); t2=$(ps -eLf | wc -l); f=$(lsof | wc -l); printf '\b%.0s' {1..100}; printf "$search_proc$: $t, all: $t2; files: $f"; printf '%.0s' {1..100}; printf '\b%.0s' {1..100}; sleep 0.5; done
```