---
publish: true
created: 2025-05-15T09:01:48.529+02:00
modified: 2025-05-26T15:25:06.075+02:00
published: 2025-05-26T15:25:06.075+02:00
cssclasses: ""
---


#nextcloud/recognize #tar/extract

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/35315/482223>

- download the archive using the correct version from <https://github.com/nextcloud/recognize/archive/refs/tags/v7.0.0.tar.gz>
- copy the archive into the Nextcloud container
- extract only the `models` directory into `/var/www/html/custom_apps/recognize/`

```shell
[docker-jail nextcloud]# docker compose cp recognize-7.0.0.tar.gz app:/var/www/html/custom_apps/recognize/
[docker-jail nextcloud]# docker compose exec -u www-data app bash
www-data@nextcloud:~/html$ cd custom_apps/recognize/
www-data@nextcloud:~/html/custom_apps/recognize$ tar -xf recognize-7.0.0.tar.gz recognize-7.0.0/models
www-data@nextcloud:~/html/custom_apps/recognize$ mv recognize-7.0.0/models/ .
www-data@nextcloud:~/html/custom_apps/recognize$
exit
[docker-jail nextcloud]# docker compose exec app bash
root@nextcloud:/var/www/html# rm -r custom_apps/recognize/recognize-7.0.0*
```
