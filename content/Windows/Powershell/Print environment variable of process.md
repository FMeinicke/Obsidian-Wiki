---
{"publish":true,"cssclasses":""}
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
