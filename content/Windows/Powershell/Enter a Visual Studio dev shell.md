---
{"publish":true,"created":"2025-05-15T09:01:52.029+02:00","modified":"2025-05-27T08:42:34.419+02:00","published":"2025-05-27T08:42:34.419+02:00","cssclasses":""}
---

#pwsh/import-module #enter-vsdevshell #visual-studio #msvc

> [!info] Source
> 
> - <https://discourse.cmake.org/t/best-practice-for-ninja-build-visual-studio/4653/5>
> - <https://stackoverflow.com/a/69961784/12780516>

```powershell
> $VS_PATH="C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools"
> Import-Module "$VS_PATH\Common7\Tools\Microsoft.VisualStudio.DevShell.dll"
> Enter-VsDevShell -VsInstallPath $VS_PATH -DevCmdArguments '-arch=x64'
```