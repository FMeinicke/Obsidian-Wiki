---
{"publish":true,"cssclasses":""}
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