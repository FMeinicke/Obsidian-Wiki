---
{"publish":true,"cssclasses":""}
---

#vmware/vmx #side-channel-mitigations

> [!info] Source
> 
> - <https://www.reddit.com/r/vmware/comments/j2fyfl/comment/g87z5y5/>

- add the following to the VM's `.vmx` file

```ini
ulm.disableMitigations = "TRUE"
```