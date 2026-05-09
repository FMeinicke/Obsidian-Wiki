---
publish: true
created: 2024-12-06T06:58:15.107+01:00
modified: 2025-05-26T17:02:42.000+02:00
published: 2025-05-26T17:02:42.000+02:00
---

#psql #docker-compose/exec #vjournal

> [!info] Source(s)
>
> - <https://help.nextcloud.com/t/synchronizing-notes-over-caldav-as-vjournal-format/1676/17>

```shell
[docker-jail nextcloud]# docker compose exec db bash
root@030f910692ae:/# psql nextcloud nextcloud_pg
psql (16.3 (Debian 16.3-1.pgdg120+1))
Type "help" for help.

nextcloud=# \d oc_calendars
...
nextcloud=# select id,principaluri,uri,components from oc_calendars;
# note the id of the calendar to edit, let's say it's 4
nextcloud=# update oc_calendars set components='VEVENT,VTODO,VJOURNAL' where id=4;
UPDATE 1
nextcloud=# select id,principaluri,uri,components from oc_calendars;
# check that the 'components' column now lists the 'VJOURNAL' capability
```
