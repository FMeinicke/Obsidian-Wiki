---
{"publish":true,"created":"2025-05-15T09:01:51.686+02:00","modified":"2025-05-27T08:42:33.654+02:00","published":"2025-05-27T08:42:33.654+02:00","cssclasses":""}
---

#hyper-v #display #pwsh/set-vmvideo

> [!info] Source
> 
> - <https://learn.microsoft.com/en-us/answers/questions/341631/how-to-adjust-virtual-machine-display-resolution-t>

```powershell
Set-VMVideo -VMName "Name of VM in Manager" -HorizontalResolution 1920 -VerticalResolution 1080 -ResolutionType Single
```