---
{"publish":true,"cssclasses":"hide_properties"}
---


- [Bind mount in top-level `volumes`](Docker/Bind mount in top-level `volumes`.md)
- [Change Docker data directory](Docker/Change Docker data directory.md)
- [CIFS share as volume](Docker/CIFS share as volume.md)
- [Error response from daemon endpoint with name already exists in network](Docker/Error response from daemon endpoint with name already exists in network.md)
- [Limit container resources in docker-compose.yml](Docker/Limit container resources in docker-compose.yml.md)
- [Making small changes to existing images without rebuilding from a Dockerfile](Docker/Making small changes to existing images without rebuilding from a Dockerfile.md)
- [Modify `sysctl` parameters inside containers](Docker/Modify `sysctl` parameters inside containers.md)
- [Print all dangling image IDs](Docker/Print all dangling image IDs.md)
- [Running systemd as PID 1 in a container](Docker/Running systemd as PID 1 in a container.md)
- [Transferring an image between hosts](Docker/Transferring an image between hosts.md)
- [WSL `error getting credentials - err exec docker-credential-desktop.exe executable file not found in $PATH, out`](Docker/WSL `error getting credentials - err exec docker-credential-desktop.exe executable file not found in $PATH, out`.md)

---


#wsl #docker-desktop #credentials

> [!info] Source
>
> - <https://forums.docker.com/t/docker-credential-desktop-exe-executable-file-not-found-in-path-using-wsl2/100225/5>

- change `credsStore` to `credStore` in `~/.docker/config.json`

  ```shell
  sed -i 's/credsStore/credStore/' ~/.docker/config.json
  ```

- or remove `"credsStore"` if it is present in `~/.docker/config.json`


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


#docker/image/ls #docker/filter #docker/format #docker/image/dangling #jq #docker/image/rm

> [!info] Source
> 
> - <https://docs.docker.com/reference/cli/docker/image/ls/#filter>

```shell
docker image ls --filter "dangling=true" --format json | jq -r '.ID'
# to remove them
docker image rm $(docker image ls --filter "dangling=true" --format json | jq -r '.ID')
```


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


#docker/run/--privileged #linux/sysctl

> [!info] Source
> 
> - <https://stackoverflow.com/a/70039423/12780516>

- launch the container with the `--privileged` option



#docker/run #docker/run/--privileged #docker/run/--tmpfs #dockerfile #docker-compose #docker-compose/tmpfs #docker-compose/privileged #ubuntu #systemd 

> [!info] Source
> 
> - <https://github.com/AkihiroSuda/containerized-systemd/blob/47070057becab3f44771b676e9c400289405b0cd/Dockerfile.ubuntu-20.04>
> - <https://github.com/solita/docker-systemd>
> - <https://forums.docker.com/t/docker-run-privileged-systemd-kills-all-tty-sessions/8610/3>

The most basic setup requires the following Dockerfile (taken from [AkihiroSuda/containerized-systemd/Dockerfile.ubuntu-20.04] in combination with the `CMD` from [solita/docker-systemd]):

```Dockerfile
FROM ubuntu:latest
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  systemd systemd-sysv dbus dbus-user-session
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal auto noprompt 3>&1"]
```

Running a container from that image requires the following command:

```shell
docker run --name ubuntu-systemd --privileged -d --tmpfs /tmp --tmpfs /run --tmpfs /run/lock bash
```

Note that mounting the `/sys/fs/cgroup` tree is not required (and would actually cause problems, resulting in the container to immediately exit after starting).

This setup, however, hijacks the host system's (login) TTY, which is not ideal. To circumventing this issue, masking some systemd services in the Dockerfile prevents spawning the `getty` service inside the container so that no login shell is created that could interfere with the host's TTY.

```Dockerfile
FROM ...
RUN ...
RUN systemctl mask systemd-logind.service getty.service getty.target
CMD ...
```

Using this (or a derived) image with a Docker compose project would have to use the following compose file:

```yaml
services:
  ubuntu-systemd:
    image: ubuntu-systemd:latest
    privileged: true
    tmpfs:
      - /tmp
      - /run
      - /run/lock
    restart: unless-stopped
```

[solita/docker-systemd]: https://github.com/solita/docker-systemd
[AkihiroSuda/containerized-systemd/Dockerfile.ubuntu-20.04]: https://github.com/AkihiroSuda/containerized-systemd/blob/47070057becab3f44771b676e9c400289405b0cd/Dockerfile.ubuntu-20.04




#docker/image/save #docker/image/load

> [!info] Source
> 
> - GitHub Copilot sugestion

To easily transfer an image from one host to another, we can save the image on the first host to a tar archive, copy this to the other host, and load the image there.

```shell
# on the first host
docker image save <image:tag> > image.tar

## copy the tar archive to the other host (e.g. `scp` or `rsync`)

# on the second host
docker image load -i image.tar
```




#docker/run #docker/exec #docker/commit #systemctl/mask

> [!info] Source
> 
> - 

Sometimes, you might want to add a simple command in the middle of a Dockerfile but don't want to rebuild the whole image again.
In case this command is self-contained (i.e. doesn't introduce downstream dependencies to existing commands later in the Dockerfile), you can create an updated image using the following procedure:

1. Run a temporary container from the existing image.
2. Execute the command to be added in that container in an interactive shell session.
3. Commit the changed container to an image (ideally using the same name and tag as the existing one to be a drop-in replacement for running containers already using that existing image, so that they can simply be recreated using the new image).
4. Recreate and restart any affected containers using this image.
5. Add the command to the Dockerfile at the desired location.

For example, given the first Dockerfile from [[Docker/Running systemd as PID 1 in a container\|Running systemd as PID 1 in a container]] with the image named `ubuntu-systemd:latest` and the `systemcl mask` command to be added using the described procedure, you'd need to do the following:

```console
root@svr-vm-docker-01:/# docker run --name ubuntu-systemd-temp -d ubuntu-systemd:latest
root@svr-vm-docker-01:/# docker exec -ti ubuntu-systemd-temp bash
root@d1849fe4a768:/# systemctl mask systemd-logind.service getty.service getty.target
root@d1849fe4a768:/# exit
root@svr-vm-docker-01:/# docker commit ubuntu-systemd-temp ubuntu-systemd:latest
```




#docker/daemon #rsync

> [!info] Source
> 
> - <https://blog.adriel.co.nz/2018/01/25/change-docker-data-directory-in-debian-jessie/>

- Stop the docker daemon and ensure no docker process is running
  
  ```console
  # systemctl stop docker
  $ ps aux | grep -i docker
  ```
  
- Copy the `/var/lib/docker` tree to the new location
  
  ```console
  # rsync -aPS /var/lib/docker/ /mnt/hdd-tank/docker-data-root
  ```
  
  Be sure to `--exclude` any locally bind-mounted directories.
- Change the directory in the Docker configuration file (`/etc/docker/daemon.json`)
  ```json
  {
    ...
    "data-root": "/mnt/hdd-tank/docker-data-root",
    ...
  }
  ```
  
  Alternatively, create a symlink from `/var/lib/docker` to the new data directory. In this case no change to the configuration file is required.
  
- Restart the docker daemon and verify the new location is being used, and that all containers are running as expected
  
  ```console
  # systemctl start docker
  $ docker info | grep Docker Root Dir
  $ docker ps -a
  ```
  
- If everything is running smoothly for a few days, remove the `/var/lib/docker` tree
  
  ```console
  # rm -rf /var/lib/docker
  ```


---

## Tagged mentions


