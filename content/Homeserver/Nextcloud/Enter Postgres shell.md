---
publish: true
created: 2024-12-06T06:58:19.520+01:00
modified: 2025-05-26T17:03:10.000+02:00
published: 2025-05-26T17:03:10.000+02:00
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
