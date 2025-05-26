---
{"publish":true,"cssclasses":""}
---


#motd #message-fo-the-day #welcome-message #greeting #bash

> [!info] Source
>
>

```shell
echo -e '#!/bin/sh\necho\nip a s' | sudo tee /etc/update-motd.d/20-ip
sudo chmod +x /etc/update-motd.d/20-ip
```