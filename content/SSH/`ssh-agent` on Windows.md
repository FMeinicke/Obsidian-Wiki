---
{"publish":true,"created":"2025-05-15T09:01:51.420+02:00","modified":"2025-05-26T15:25:13.044+02:00","published":"2025-05-26T15:25:13.044+02:00","cssclasses":""}
---

#ssh #ssh-agent #ssh-add #ssh/key #pwsh/set-service #pwsh/start-service #windows

> [!info] Source
>
>

```powershell
> Set-Service ssh-agent -StartupType Automatic
> Start-Service ssh-agent
```

Then add keys to the agent as usual with

```powershell
> ssh-add ~\.ssh\id_rsa
```