---
publish: true
created: 2024-12-06T06:58:23.893+01:00
modified: 2025-05-26T17:03:51.000+02:00
published: 2025-05-26T17:03:51.000+02:00
---

#ssh #ssh-agent #ssh-add #ssh/key #pwsh/set-service #pwsh/start-service #windows

> [!info] Source

```powershell
> Set-Service ssh-agent -StartupType Automatic
> Start-Service ssh-agent
```

Then add keys to the agent as usual with

```powershell
> ssh-add ~\.ssh\id_rsa
```
