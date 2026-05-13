---
publish: true
created: 2025-05-15T09:01:47.154+02:00
modified: 2025-05-26T15:25:03.214+02:00
published: 2025-05-26T15:25:03.214+02:00
cssclasses: ""
---

#docker-compose/deploy/resources/limits

> [!info] Source
> 
> - <https://stackoverflow.com/a/57135933/12780516>

```yaml
  deploy:
    resources:
      limits:
        cpus: '0.001'
        memory: 50M
```