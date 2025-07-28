---
{"publish":true,"created":"2025-05-15T09:01:50.061+02:00","modified":"2025-05-26T15:25:09.638+02:00","published":"2025-05-26T15:25:09.638+02:00","cssclasses":""}
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