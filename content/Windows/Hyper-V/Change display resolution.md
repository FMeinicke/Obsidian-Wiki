---
{"publish":true,"cssclasses":""}
---

#hyper-v #display #pwsh/set-vmvideo

> [!info] Source
> 
> - <https://learn.microsoft.com/en-us/answers/questions/341631/how-to-adjust-virtual-machine-display-resolution-t>

```powershell
Set-VMVideo -VMName "Name of VM in Manager" -HorizontalResolution 1920 -VerticalResolution 1080 -ResolutionType Single
```