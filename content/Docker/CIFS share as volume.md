---
publish: true
created: 2024-12-06T06:58:23.543+01:00
modified: 2025-05-26T17:03:49.000+02:00
published: 2025-05-26T17:03:49.000+02:00
---

#docker-compose/volumes/cifs

> [!info] Source
>
> -

```yaml
version: '3'

volumes:
  gitlab-backup:
    driver: local
    driver_opts:
      type: "cifs"
      device: "//192.168.101.56/gitlab-backup"
      o: "addr=192.168.101.56,vers=3.0,username=Buildserver,password=1buildserver9,rw,noatime,nolease,uid=998,gid=998,dir_mode=0700,file_mode=0766"
```
