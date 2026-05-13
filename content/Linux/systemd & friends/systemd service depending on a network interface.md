---
publish: true
created: 2025-05-15T09:01:51.061+02:00
modified: 2025-05-26T15:25:11.825+02:00
published: 2025-05-26T15:25:11.825+02:00
cssclasses: ""
---

#systemd #systemd-unit #systemd-service #network

> [!info] Source
>
> - <https://unix.stackexchange.com/a/227768>

- use `BindsTo=` and `After=` in the `[Unit]` section and `WantedBy=` in `[Install]`

  ```systemd
  [Unit]
  Description=Service depending on interface %I
  Wants=network-online.target
  BindsTo=sys-subsystem-net-devices-%i.device
  After=multi-user.target sys-subsystem-net-devices-%i.device network-online.target

  [Service]
  Type=simple
  ExecStart=...

  [Install]
  WantedBy=default.target sys-subsystem-net-devices-%i.device
  ```

- use `Wants=network-online.target` and `After=network-online.target` to actually wait for the network to be online
  > [!NOTE]
  > This only works as a one-time concept during system start-up. The `network-online.service` unit does not monitor the online state of the system!