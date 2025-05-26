---
{"publish":true,"cssclasses":""}
---


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
