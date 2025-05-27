---
{"publish":true,"cssclasses":""}
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