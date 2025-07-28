---
{"publish":true,"created":"2025-05-15T09:01:51.623+02:00","modified":"2025-05-27T08:42:33.529+02:00","published":"2025-05-27T08:42:33.529+02:00","cssclasses":""}
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