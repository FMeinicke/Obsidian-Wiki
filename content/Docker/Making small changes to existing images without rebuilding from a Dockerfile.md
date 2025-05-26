---
{"publish":true,"cssclasses":""}
---


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
