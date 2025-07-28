---
{"publish":true,"created":"2025-05-15T09:01:52.201+02:00","modified":"2025-05-27T08:42:34.810+02:00","published":"2025-05-27T08:42:34.810+02:00","cssclasses":""}
---

#pwsh/get-childitem #pwsh/foreach-object

> [!info] Source
> 
> - <https://superuser.com/a/914980/1201131>

```powershell
Get-ChildItem -Filter "<pattern>" -Recurse $pwd
```

to do something with the found files/folders, e.g. deleting

```powershell
Get-ChildItem -Filter "<pattern>" -Recurse $pwd | ForEach-Object { rm -r $_ }
```