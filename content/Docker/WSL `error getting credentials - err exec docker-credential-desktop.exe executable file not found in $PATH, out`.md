---
publish: true
created: 2024-12-06T06:58:08.911+01:00
modified: 2025-05-26T17:01:59.000+02:00
published: 2025-05-26T17:01:59.000+02:00
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
