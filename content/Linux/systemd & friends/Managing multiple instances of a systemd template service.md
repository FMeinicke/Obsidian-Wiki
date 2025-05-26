---
{"publish":true,"cssclasses":""}
---

#systemd #systemd-service #service-template #instanced-service

> [!info] Source
>
>

- Use the `<service_name>*` syntax to operate on all services of the `<service_name>@.service` template, e.g.

  ```shell
  sudo systemctl start 'sila_cetoni*'
  ```

  will start all instanced services of the `sila_cetoni@.service` template
- this works for the systemd commands `start`, `stop`, `restart` and `status` (maybe for others too but this has not been tested yet)