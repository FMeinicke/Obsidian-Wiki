---
publish: true
created: 2024-12-06T06:58:19.227+01:00
modified: 2025-05-26T17:03:10.000+02:00
published: 2025-05-26T17:03:10.000+02:00
---

#motd #message-fo-the-day #welcome-message #greeting #bash

> [!info] Source

```shell
echo -e '#!/bin/sh\necho\nip a s' | sudo tee /etc/update-motd.d/20-ip
sudo chmod +x /etc/update-motd.d/20-ip
```
