---
{"publish":true,"cssclasses":""}
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