---
{"publish":true,"cssclasses":""}
---

#pwsh/foreach-object #pwsh/split #pwsh/tostring

> [!info] Source
> 
> - <https://stackoverflow.com/a/24634448/12780516>

```powershell
Get-Content filename | ForEach-Object { $_.Split(" ")[1] }
```

(`$_` might not be a string, in which case it needs to be converted to one using `$_.toString()`)