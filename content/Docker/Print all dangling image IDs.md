---
{"publish":true,"created":"2025-05-15T09:01:47.216+02:00","modified":"2025-05-26T15:25:03.355+02:00","published":"2025-05-26T15:25:03.355+02:00","cssclasses":""}
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