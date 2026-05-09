---
publish: true
created: 2024-12-06T06:58:14.634+01:00
modified: 2025-05-26T17:02:37.000+02:00
published: 2025-05-26T17:02:37.000+02:00
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
