---
publish: true
created: 2025-08-15T09:13:03.030+02:00
modified: 2025-09-24T17:18:53.000+02:00
published: 2025-09-24T17:18:53.000+02:00
cssclasses: ""
---


#nextcloud #apache2

> [!info] Source
> 
> - <https://askubuntu.com/a/396048>

- my Nextcloud shows `apache2: Could not reliably determine the server's fully qualified domain name`
- to fix this, add `ServerName nextcloud.example.com` to `/etc/apache2/apache2.conf` and then reload/restart the server
