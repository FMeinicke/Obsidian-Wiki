---
{"publish":true,"created":"2025-05-15T09:01:47.060+02:00","modified":"2025-05-26T15:25:02.996+02:00","published":"2025-05-26T15:25:02.996+02:00","cssclasses":""}
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