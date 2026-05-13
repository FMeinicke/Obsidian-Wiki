---
publish: true
created: 2025-05-15T09:01:52.123+02:00
modified: 2025-05-27T08:42:34.654+02:00
published: 2025-05-27T08:42:34.654+02:00
cssclasses: ""
---


#pwsh/get-process #python/psutil/Process #environment-variables

> [!info] Source
> 
> - <https://superuser.com/a/1756391/1201131>
> - <https://ollama.lancetoni.local/c/3e9b5440-b2f6-4477-a7d3-a3dbbd39ad8b>

```powershell
$proc_id = (Get-Process -Name "<NAME>").Id; python -c "import psutil; print(psutil.Process(pid=$proc_id).environ()['PATH'])"
```

replace `<NAME>` with the process name and optionally `PATH` with another environment variable name
