---
publish: true
created: 2025-05-15T09:01:50.279+02:00
modified: 2025-05-26T15:25:10.278+02:00
published: 2025-05-26T15:25:10.278+02:00
cssclasses: ""
---


#motd #message-fo-the-day #welcome-message #greeting #bash

> [!info] Source
>
>

```shell
echo -e '#!/bin/sh\necho\nip a s' | sudo tee /etc/update-motd.d/20-ip
sudo chmod +x /etc/update-motd.d/20-ip
```