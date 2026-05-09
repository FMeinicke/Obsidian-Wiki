---
publish: true
created: 2024-12-06T06:58:09.641+01:00
modified: 2025-05-26T17:02:10.000+02:00
published: 2025-05-26T17:02:10.000+02:00
---

#systemd #systemd-service #service-template #instanced-service

> [!info] Source

- Use the `<service_name>*` syntax to operate on all services of the `<service_name>@.service` template, e.g.

  ```shell
  sudo systemctl start 'sila_cetoni*'
  ```

  will start all instanced services of the `sila_cetoni@.service` template
- this works for the systemd commands `start`, `stop`, `restart` and `status` (maybe for others too but this has not been tested yet)
