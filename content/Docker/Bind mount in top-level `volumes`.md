---
{"publish":true,"cssclasses":""}
---

#docker-compose/volumes/local

> [!info] Source
> 
> - <https://forums.docker.com/t/top-level-volume-with-absolute-path/27552/6>

```yaml
version: '3'

volumes:
  config:
    driver: local
    driver_opts:
      type: local
      device: ./volumes/<service>/data
      o: bind
```