---
{"publish":true,"cssclasses":""}
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