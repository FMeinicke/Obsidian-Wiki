---
{"publish":true,"cssclasses":""}
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