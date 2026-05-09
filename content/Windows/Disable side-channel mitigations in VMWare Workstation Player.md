---
publish: true
created: 2024-12-06T06:58:11.034+01:00
modified: 2025-05-27T08:42:41.000+02:00
published: 2025-05-27T08:42:41.000+02:00
---

#vmware/vmx #side-channel-mitigations

> [!info] Source
>
> - <https://www.reddit.com/r/vmware/comments/j2fyfl/comment/g87z5y5/>

- add the following to the VM's `.vmx` file

```ini
ulm.disableMitigations = "TRUE"
```
