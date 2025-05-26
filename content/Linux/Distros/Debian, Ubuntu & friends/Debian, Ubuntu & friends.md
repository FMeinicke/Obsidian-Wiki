---
publish: true
sorting-spec: |-
  Debian, Ubuntu & friends
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Change the system editor using `update-alternatives`](Linux/Distros/Debian, Ubuntu & friends/Change the system editor using `update-alternatives`.md)
- [Find out the package that provides a file](Linux/Distros/Debian, Ubuntu & friends/Find out the package that provides a file.md)
- [Find out what packages depend on a package](Linux/Distros/Debian, Ubuntu & friends/Find out what packages depend on a package.md)
- [Fix a debian package that is not completely installed](Linux/Distros/Debian, Ubuntu & friends/Fix a debian package that is not completely installed.md)
- [Fix a debian package's maintainer scripts](Linux/Distros/Debian, Ubuntu & friends/Fix a debian package's maintainer scripts.md)
- [Install a specific version of a package](Linux/Distros/Debian, Ubuntu & friends/Install a specific version of a package.md)

---



#debian #ubuntu #deb #deb-package #preinst #postinst #prerm

> [!info] Source
>
> - <https://unix.stackexchange.com/a/138190>

- unpack the .deb archive to a temporary directory

  ```shell
  mkdir tmp
  sudo dpkg-deb -R my-package.deb tmp
  ```

- edit the scripts inside the temporary directory
- optionally: fix the permissions on the maintainer scripts to be `>=0555` and `<=0755`, e.g.

  ```shell
  sudo chmod 0755 tmp/DEBIAN/preinst
  ```

- package the files in the temporary directory into a .deb archive again

  ```shell
  sudo dpkg-deb -b tmp my-package-fixed.deb
  ```

- then simply install the fixed package as usual

  ```shell
  sudo apt-get install ./my-package-fixed.deb
  ```



#debian #ubuntu #deb #deb-package #broken-install #failed-install

> [!info] Source
>
> - <https://askubuntu.com/a/632523>



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



#update-alternatives #editor #vim

> [!info] Source
> 
> - <https://askubuntu.com/a/891931/1152691>

```console
$ sudo update-alternatives --config editor
[sudo] password for user1:
There are 3 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path               Priority   Status
------------------------------------------------------------
* 0            /bin/nano           40        auto mode
  1            /bin/nano           40        manual mode
  2            /usr/bin/mcedit     25        manual mode
  3            /usr/bin/vim.tiny   15        manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
```

- note that if `vim` doesn't show up in this menu, it probably means that it points to `vim.tiny` (or `vim.basic`)

```console
$ ll $(which vim)
lrwxrwxrwx 1 root root 26 May  4  2023 /usr/bin/vim -> /etc/alternatives/vim.tiny*
```



#apt #dpk/-S

> [!info] Source
> 
> - <https://www.cyberciti.biz/faq/equivalent-of-rpm-qf-command/>

```shell
dpkg -S <package>
```



#apt #apt-cache/rdepends

> [!info] Source
> 
> - <https://askubuntu.com/a/128527/1152691>

```shell
apt-cache rdepends [--installed] <package>
```

---

## Tagged mentions


