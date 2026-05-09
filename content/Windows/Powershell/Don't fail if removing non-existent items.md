---
publish: true
created: 2024-12-06T06:58:12.084+01:00
modified: 2025-05-27T08:42:41.000+02:00
published: 2025-05-27T08:42:41.000+02:00
---

#pwsh/remove-item #pwsh/-error-action

> [!info] Source
>
> - <https://stackoverflow.com/a/63157816/12780516>

- use `-ErrorAction Ignore` (return code will be success), or `-ErrorAction SilentlyContinue` (return code will be failure, but not error be raised)

```powershell
Remove-Item <Path> -ErrorAction Ignore
```
