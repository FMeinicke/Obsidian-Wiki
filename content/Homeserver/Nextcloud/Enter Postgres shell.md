---
{"publish":true,"cssclasses":""}
---


#psql #docker-compose/exec

> [!info] Source(s)
> 
> - 

```shell
[docker-jail nextcloud]# docker compose exec db bash
root@030f910692ae:/# psql nextcloud nextcloud_pg
psql (16.3 (Debian 16.3-1.pgdg120+1))
Type "help" for help.

nextcloud=# \d        # for example
```