---
{"publish":true,"created":"2025-08-15T09:08:34.243+02:00","modified":"2025-08-15T09:12:37.826+02:00","published":"2025-08-15T09:12:37.826+02:00","cssclasses":""}
---


#nextcloud #postgres #psql 

> [!info] Source
> 
> - <https://help.nextcloud.com/t/nextcloud-postgres-redis-in-docker-collation-version-mismatch/164294/3>

- stop the Nextcloud container
  
  ```console
  $ docker compose stop app
  ```
  
- bash into the postgres container and refresh the collation version, then reindex the database (this takes a while, don't worry)
  
  ```console
  $ docker compose exec db bash
  root@9460dcc37889:/# psql -U nextcloud_pg nextcloud
  WARNING:  database "nextcloud" has a collation version mismatch
  DETAIL:  The database was created using collation version 2.36, but the operating system provides version 2.41.
  HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE nextcloud REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
  psql (16.10 (Debian 16.10-1.pgdg13+1))
  Type "help" for help.
    
  nextcloud=# ALTER DATABASE nextcloud REFRESH COLLATION VERSION;
  NOTICE:  changing version from 2.36 to 2.41
  ALTER DATABASE
  nextcloud=# REINDEX DATABASE nextcloud;
  REINDEX
  nextcloud=#
  \q
  root@9460dcc37889:/#
  exit
  ```
  
- restart the nextcloud container
  
  ```console
  $ docker compose up -d
  ```
  
