---
publish: true
created: 2025-07-04T08:16:05.776+02:00
modified: 2025-05-28T08:38:23.000+02:00
published: 2025-05-28T08:38:23.000+02:00
---

#docker/context/create #docker/--context #docker/compose

> [!info] Source
>
> - <https://docs.docker.com/engine/daemon/remote-access/>
> - <https://docs.docker.com/engine/security/protect-access/>

- when using SSH no additional configuration is required on the remote host and the connection is secure by default
- also, your `~/.ssh/config` is respected so that you can use the hosts defined there without having to specify the user, port, identity file, etc.

```console
$ docker context create remote-host --docker ssh://my-host
$ docker --context remote-host ps -a
...
```

(this expects a properly configured host named `my-host` in your `~/.ssh/config`)

- for better convenience, create an alias so that you can easily use the context with `compose` commands as well

```console
$ echo 'alias docker-rh="docker --context remote-host"' >> ~/.bash_rc
$ . ~/.bash_rc
$ docker-rh compose ps -a
...
```
