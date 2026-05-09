---
publish: true
created: 2024-12-06T06:58:19.977+01:00
modified: 2025-05-26T17:03:13.000+02:00
published: 2025-05-26T17:03:13.000+02:00
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
