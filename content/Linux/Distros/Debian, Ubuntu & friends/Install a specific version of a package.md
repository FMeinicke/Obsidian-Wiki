---
{"publish":true,"created":"2025-05-15T09:01:50.076+02:00","modified":"2025-05-26T15:25:09.700+02:00","published":"2025-05-26T15:25:09.700+02:00","cssclasses":""}
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