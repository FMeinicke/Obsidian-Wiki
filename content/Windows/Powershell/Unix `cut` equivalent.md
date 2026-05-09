---
publish: true
created: 2024-12-06T06:58:20.067+01:00
modified: 2025-05-27T08:42:49.000+02:00
published: 2025-05-27T08:42:49.000+02:00
---

#pwsh/foreach-object #pwsh/split #pwsh/tostring

> [!info] Source
>
> - <https://stackoverflow.com/a/24634448/12780516>

```powershell
Get-Content filename | ForEach-Object { $_.Split(" ")[1] }
```

(`$_` might not be a string, in which case it needs to be converted to one using `$_.toString()`)
