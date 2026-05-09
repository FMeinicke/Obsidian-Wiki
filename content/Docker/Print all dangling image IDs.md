---
publish: true
created: 2024-12-06T06:58:21.700+01:00
modified: 2025-05-26T17:03:28.000+02:00
published: 2025-05-26T17:03:28.000+02:00
---

#docker/image/ls #docker/filter #docker/format #docker/image/dangling #jq #docker/image/rm

> [!info] Source
>
> - <https://docs.docker.com/reference/cli/docker/image/ls/#filter>

```shell
docker image ls --filter "dangling=true" --format json | jq -r '.ID'
# to remove them
docker image rm $(docker image ls --filter "dangling=true" --format json | jq -r '.ID')
```
