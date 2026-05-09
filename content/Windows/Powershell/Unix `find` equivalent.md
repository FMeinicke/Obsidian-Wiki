---
publish: true
created: 2024-12-06T06:58:19.844+01:00
modified: 2025-05-27T08:42:48.000+02:00
published: 2025-05-27T08:42:48.000+02:00
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
