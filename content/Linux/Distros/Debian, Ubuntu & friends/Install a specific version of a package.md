---
publish: true
created: 2024-12-06T06:58:09.998+01:00
modified: 2025-05-26T17:02:17.000+02:00
published: 2025-05-26T17:02:17.000+02:00
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
