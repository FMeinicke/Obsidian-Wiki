---
publish: true
created: 2024-12-06T06:58:16.044+01:00
modified: 2025-05-27T08:42:45.000+02:00
published: 2025-05-27T08:42:45.000+02:00
---

#pwsh/expansion

> [!info] Source
>
> - <https://stackoverflow.com/a/16224670/12780516>

```powershell
PS C:\> "test","dev","prod" | % { "server-$_" }
server-test
server-dev
server-prod
PS C:\> 1..5 | % { "server{0:D2}" -f $_ }
server01
server02
server03
server04
server05
PS C:\> 1..5 | % { "192.168.0.$_" }
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
```

Note that `%` is an alias for the `ForEach-Object` cmdlet.
