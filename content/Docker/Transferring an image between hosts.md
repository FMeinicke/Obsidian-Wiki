---
{"publish":true,"cssclasses":""}
---


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
