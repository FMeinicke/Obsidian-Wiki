---
publish: true
created: 2024-12-06T06:58:09.998+01:00
modified: 2025-05-26T17:02:15.000+02:00
published: 2025-05-26T17:02:15.000+02:00
---

#docker/network/disconnect #docker/compose/up/-d #nextcloud

> [!info] Source
>
> - trial and error
> - <https://github.com/moby/moby/issues/33156>

- remove the container from the network explicitly

```shell
$ docker compose up -d
[+] Running 0/1
 ⠏ Container nextcloud-db-1  Starting
Error response from daemon: endpoint with name nextcloud-db-1 already exists in network nextcloud_backend
$ docker network disconnect nextcloud_backend nextcloud-db-1
$ docker compose up -d
[+] Running 1/1
 ✔ Container nextcloud-db-1  Started
```

- otherwise try to remove the network and let compose create it again
- if a non-existent container prevents the network from being removed, restarting the docker service is currently the only option (<https://github.com/moby/moby/issues/33156>)
  - first `docker compose down` the affected stack, there will be an error that the affected network cannot be removed
  - then restart docker
  - afterward remove the affected network manually `docker network rm <network>`
  - now bring the stack back up again
