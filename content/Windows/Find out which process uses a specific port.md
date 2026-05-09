---
publish: true
created: 2024-12-06T06:58:15.897+01:00
modified: 2025-05-27T08:42:45.000+02:00
published: 2025-05-27T08:42:45.000+02:00
---

#port #pwsh/get-process #pwsh/get-nettcpconnection #pwsh/get-netudpendpoint #tcp #udp

> [!info] Source
>
> - <https://stackoverflow.com/a/48199/12780516>

- for TCP connections

  ```powershell
  Get-Process -Id (Get-NetTCPConnection -LocalPort <PORT>).OwningProcess
  ```

- for UDP connections

  ```powershell
  Get-Process -Id (Get-NetUDPEndpoint -LocalPort <PORT>).OwningProcess
  ```
