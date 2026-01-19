---
publish: true
created: 2025-05-15T09:01:52.170+02:00
modified: 2025-05-27T08:42:34.763+02:00
published: 2025-05-27T08:42:34.763+02:00
cssclasses: ""
---

#pwsh/foreach-object #pwsh/split #pwsh/tostring

> [!info] Source
> 
> - <https://stackoverflow.com/a/24634448/12780516>

```powershell
Get-Content filename | ForEach-Object { $_.Split(" ")[1] }
```

(`$_` might not be a string, in which case it needs to be converted to one using `$_.toString()`)