---
{"publish":true,"created":"2025-05-15T09:01:48.576+02:00","modified":"2025-05-26T15:25:06.200+02:00","published":"2025-05-26T15:25:06.200+02:00","cssclasses":""}
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