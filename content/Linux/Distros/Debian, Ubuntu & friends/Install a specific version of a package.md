---
{"publish":true,"cssclasses":""}
---


#apt/install #apt-cache/show #version

> [!info] Source
> 
> - <https://askubuntu.com/a/428778/1152691>
> - <https://stackoverflow.com/a/38567493/12780516>

```shell
sudo apt install <package>=<version>
```

- to find available versions

```shell
apt-cache show <package> | grep -i version
```