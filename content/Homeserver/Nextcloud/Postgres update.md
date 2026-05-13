---
publish: true
created: 2025-05-15T09:01:48.654+02:00
modified: 2025-05-26T15:25:06.372+02:00
published: 2025-05-26T15:25:06.372+02:00
cssclasses: ""
---


#nextcloud #postgres #pg_dump #pg_dumpall #psql

> [!info] Source
> 
> - Backup and restore postgres
>     - <https://www.cloudytuts.com/tutorials/docker/how-to-upgrade-postgresql-in-docker-and-kubernetes/>
>     - <https://docs.nextcloud.com/server/latest/admin_manual/maintenance/backup.html#postgresql>
>     - <https://docs.nextcloud.com/server/latest/admin_manual/maintenance/restore.html#postgresql>
> - Postgres 14 password error: <https://help.nextcloud.com/t/how-to-upgrade-postgresql-from-v13-to-v14-or-v15/152102/5>
> - Postgres 14 permission error: <https://help.nextcloud.com/t/how-to-upgrade-postgresql-from-v13-to-v14-or-v15/152102/6>
> - Change postgres user's password: <https://stackoverflow.com/a/15008311/12780516>

- stop nextcloud
- backup the whole database (including users, etc.)

```shell
docker compose exec -T db pg_dumpall -U $(cat buildfiles/postgres_user.txt) > pg_dumpall.sql
```

- change the docker-compose.yml file duplicating the current 'db' service, renaming it to e.g. 'old_db', incrementing the version number of the image for the new db service (still named 'db', so that nextcloud doesn't need to be touched), and creating and using a new volume for the new db service (so that in case smth. goes wrong we can easily switch back to the last working db container)
- recreate the db containers
- restore the backup in the new container (named 'db'; the old one is named 'old_db'!)

```
cat pg_dumpall.sql | docker compose exec -T db psql -U $(cat buildfiles/postgres_user.txt) template1
```

- start nextcloud and hope for the best

> [!note]
> 
> - the `-T` for `docker compose` is necessary because psql does not need a TTY when used like this; it outputs the SQL commands directly to STDOUT

> [!hint]-
> 
> - one-liner
> 
> ```shell
> docker compose exec -T old_db pg_dumpall -U $(cat buildfiles/postgres_user.txt) | docker compose exec -T db psql -U $(cat buildfiles/postgres_user.txt) template1
> ```

> [!important]-
> 
> For the upgrade from Postgres <13 to >14 the password encryption mechanism was changed leading to a `Doctrine\DBAL\Exception: Failed to connect to the database: An exception occurred in the driver: SQLSTATE[08006] [7] connection to server at "db" (172.21.0.2), port 5432 failed: FATAL:  password authentication failed for user "oc_admin" in /var/www/html/lib/private/DB/Connection.php:139` error after simply starting the nextcloud container after the restoration.
> To fix this, I needed to set the password of the `oc_admin` user to the password stored in `config/config.php` with resulted in the new encryption mechanism to be used. The other `oc_admin<NN>` users don't seem to be affected.
> 
> ```shell
> docker compose exec db psql -U $(cat buildfiles/postgres_user.txt) -d nextcloud
> psql (16.2 (Debian 16.2-1.pgdg120+2))
> Type "help" for help.
> 
> nextcloud=# \du
>                                List of roles
>   Role name   |                         Attributes
> --------------+------------------------------------------------------------
>  nextcloud_pg | Superuser, Create role, Create DB, Replication, Bypass RLS
>  oc_admin     | Create DB
>  oc_admin10   | Create DB
>  oc_admin11   | Create DB
>  oc_admin12   | Create DB
>  oc_admin13   | Create DB
>  oc_admin2    | Create DB
>  oc_admin3    | Create DB
>  oc_admin4    | Create DB
>  oc_admin5    | Create DB
>  oc_admin6    | Create DB
>  oc_admin7    | Create DB
>  oc_admin8    | Create DB
>  oc_admin9    | Create DB
> 
> nextcloud=# select * from pg_shadow;
>    usename    | usesysid | usecreatedb | usesuper | userepl | usebypassrls |               passwd                | valuntil | useconfig
> --------------+----------+-------------+----------+---------+--------------+-------------------------------------+----------+-----------
>  nextcloud_pg |       10 | t           | t        | t       | t            | md56b41102633f3d550ea97321d22c4e265 |          |
>  oc_admin     |    16385 | t           | f        | f       | f            | md582d8c438d2bb02d6f362ce8a2c201381 |          |
>  oc_admin10   |    16386 | t           | f        | f       | f            | md5381c8c875b3d62140819a653a7239a08 |          |
>  oc_admin11   |    16387 | t           | f        | f       | f            | md58a4f6102232218eadae7188cc1a0bb55 |          |
>  oc_admin12   |    16388 | t           | f        | f       | f            | md52dccbdf17406afd9195f91420e242654 |          |
>  oc_admin13   |    16389 | t           | f        | f       | f            | md59a8a009f3f648c5cafe50c00ebe60b6e |          |
>  oc_admin2    |    16390 | t           | f        | f       | f            | md5176b02fa6b0c7dc7c5cca277dcd3449c |          |
>  oc_admin3    |    16391 | t           | f        | f       | f            | md564f4d8f1b30e64f571c8624c5aaf2ec8 |          |
>  oc_admin4    |    16392 | t           | f        | f       | f            | md540cbb3f4637e90621a83ccb12e87a9f7 |          |
>  oc_admin5    |    16393 | t           | f        | f       | f            | md538ac124e4669957c68daf4bc7e652e9f |          |
>  oc_admin6    |    16394 | t           | f        | f       | f            | md5d8859b0104c6b36a93560b08cb2ac973 |          |
>  oc_admin7    |    16395 | t           | f        | f       | f            | md542abecf83a402767fef8110a4b635f9d |          |
>  oc_admin8    |    16396 | t           | f        | f       | f            | md557e350dd6706a1b54e663e3510455806 |          |
>  oc_admin9    |    16397 | t           | f        | f       | f            | md51b627d32aed61221cf885043e93bb259 |          |
> (14 rows)
> 
> nextcloud=# ALTER USER oc_admin WITH PASSWORD 'krx4zr3g573gvvt76ciao15jrbzujb';
> ALTER ROLE
> nextcloud=# select * from pg_shadow;
>    usename    | usesysid | usecreatedb | usesuper | userepl | usebypassrls |                                                                passwd                                                                 | valuntil | useconfig
> --------------+----------+-------------+----------+---------+--------------+---------------------------------------------------------------------------------------------------------------------------------------+----------+-----------
>  nextcloud_pg |       10 | t           | t        | t       | t            | md56b41102633f3d550ea97321d22c4e265                                                                                                   |          |
>  oc_admin10   |    16386 | t           | f        | f       | f            | md5381c8c875b3d62140819a653a7239a08                                                                                                   |          |
>  oc_admin11   |    16387 | t           | f        | f       | f            | md58a4f6102232218eadae7188cc1a0bb55                                                                                                   |          |
>  oc_admin12   |    16388 | t           | f        | f       | f            | md52dccbdf17406afd9195f91420e242654                                                                                                   |          |
>  oc_admin13   |    16389 | t           | f        | f       | f            | md59a8a009f3f648c5cafe50c00ebe60b6e                                                                                                   |          |
>  oc_admin2    |    16390 | t           | f        | f       | f            | md5176b02fa6b0c7dc7c5cca277dcd3449c                                                                                                   |          |
>  oc_admin3    |    16391 | t           | f        | f       | f            | md564f4d8f1b30e64f571c8624c5aaf2ec8                                                                                                   |          |
>  oc_admin4    |    16392 | t           | f        | f       | f            | md540cbb3f4637e90621a83ccb12e87a9f7                                                                                                   |          |
>  oc_admin5    |    16393 | t           | f        | f       | f            | md538ac124e4669957c68daf4bc7e652e9f                                                                                                   |          |
>  oc_admin6    |    16394 | t           | f        | f       | f            | md5d8859b0104c6b36a93560b08cb2ac973                                                                                                   |          |
>  oc_admin7    |    16395 | t           | f        | f       | f            | md542abecf83a402767fef8110a4b635f9d                                                                                                   |          |
>  oc_admin8    |    16396 | t           | f        | f       | f            | md557e350dd6706a1b54e663e3510455806                                                                                                   |          |
>  oc_admin9    |    16397 | t           | f        | f       | f            | md51b627d32aed61221cf885043e93bb259                                                                                                   |          |
>  oc_admin     |    16385 | t           | f        | f       | f            | SCRAM-SHA-256$4096:l0kGUXmonwp4uTuZiL6yvg==$51J43SRvaLmPj2D9E/hYD19+tA3NExU+WcRenC9W4oI=:JI10+qC+bLwh/SjVus7dcWW/I/+WLvfjlpgPDf9iUW4= |          |
> (14 rows)
> 
> nextcloud=#
> \q
> ```
> 
> Then there was a permission error when trying to setup Memories to use database triggers: ` Insufficient privilege: 7 ERROR:  permission denied for schema public`.
> This can be fixed by granting the necessary permissions for the user `oc_admin` on the 'public' schema:
> 
> ```shell
> docker compose exec db psql -U $(cat buildfiles/postgres_user.txt) -d nextcloud
> psql (16.2 (Debian 16.2-1.pgdg120+2))
> Type "help" for help.
> 
> nextcloud=# \dnS+
>                                                   List of schemas
>         Name        |       Owner       |           Access privileges            |           Description
> --------------------+-------------------+----------------------------------------+----------------------------------
>  information_schema | nextcloud_pg      | nextcloud_pg=UC/nextcloud_pg          +|
>                     |                   | =U/nextcloud_pg                        |
>  pg_catalog         | nextcloud_pg      | nextcloud_pg=UC/nextcloud_pg          +| system catalog schema
>                     |                   | =U/nextcloud_pg                        |
>  pg_toast           | nextcloud_pg      |                                        | reserved schema for TOAST tables
>  public             | pg_database_owner | pg_database_owner=UC/pg_database_owner+| standard public schema
>                     |                   | =U/pg_database_owner                  +|
> (4 rows)
> 
> nextcloud=# GRANT ALL PRIVILEGES ON SCHEMA public TO oc_admin;
> GRANT
> nextcloud=# \dnS+
>                                                   List of schemas
>         Name        |       Owner       |           Access privileges            |           Description
> --------------------+-------------------+----------------------------------------+----------------------------------
>  information_schema | nextcloud_pg      | nextcloud_pg=UC/nextcloud_pg          +|
>                     |                   | =U/nextcloud_pg                        |
>  pg_catalog         | nextcloud_pg      | nextcloud_pg=UC/nextcloud_pg          +| system catalog schema
>                     |                   | =U/nextcloud_pg                        |
>  pg_toast           | nextcloud_pg      |                                        | reserved schema for TOAST tables
>  public             | pg_database_owner | pg_database_owner=UC/pg_database_owner+| standard public schema
>                     |                   | =U/pg_database_owner                  +|
>                     |                   | oc_admin=UC/pg_database_owner          |
> (4 rows)
> 
> nextcloud=#
> \q
> ```
> 
> (a `GRANT CREATE ...` might have been sufficient, but WTH; if it works, it works)