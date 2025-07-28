---
{"publish":true,"created":"2025-05-15T09:01:51.608+02:00","modified":"2025-05-27T08:42:33.482+02:00","published":"2025-05-27T08:42:33.482+02:00","cssclasses":""}
---

#vmware/vmx #side-channel-mitigations

> [!info] Source
> 
> - <https://www.reddit.com/r/vmware/comments/j2fyfl/comment/g87z5y5/>

- add the following to the VM's `.vmx` file

```ini
ulm.disableMitigations = "TRUE"
```