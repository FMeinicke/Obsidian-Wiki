---
{"publish":true,"created":"2025-05-15T09:01:51.998+02:00","modified":"2025-05-27T08:42:34.357+02:00","published":"2025-05-27T08:42:34.357+02:00","cssclasses":""}
---

#pwsh/remove-item #pwsh/-error-action

> [!info] Source
> 
> - <https://stackoverflow.com/a/63157816/12780516>

- use `-ErrorAction Ignore` (return code will be success), or `-ErrorAction SilentlyContinue` (return code will be failure, but not error be raised)

```powershell
Remove-Item <Path> -ErrorAction Ignore
```