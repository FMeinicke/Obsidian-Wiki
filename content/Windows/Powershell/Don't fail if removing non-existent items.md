---
{"publish":true,"cssclasses":""}
---

#pwsh/remove-item #pwsh/-error-action

> [!info] Source
> 
> - <https://stackoverflow.com/a/63157816/12780516>

- use `-ErrorAction Ignore` (return code will be success), or `-ErrorAction SilentlyContinue` (return code will be failure, but not error be raised)

```powershell
Remove-Item <Path> -ErrorAction Ignore
```