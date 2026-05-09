---
publish: true
created: 2024-12-06T06:58:21.384+01:00
modified: 2025-05-26T17:03:26.000+02:00
published: 2025-05-26T17:03:26.000+02:00
---

#ssh/config/match #ssh/config/proxycommand

> [!info] Source
>
> - <https://stackoverflow.com/a/40747254/12780516>
> - <https://man7.org/linux/man-pages/man5/ssh_config.5.html>

```conf
Host WAA-PC
  Hostname 192.168.1.2
  User WAA_Dev
  IdentityFile ~/.ssh/id_rsa_cetoni

# Use the WAA-PC as a proxy if we're not connected to the VPN directly
# (the PC has to have an active VPN connection).
Match Host gitlab.lancetoni.local Exec "ip a s tun0 >/dev/null 2>&1 && exit 1 || exit 0"
   ProxyCommand ssh -q -W %h:%p WAA-PC
Host gitlab.lancetoni.local
   Port 2222
   User git
   IdentityFile ~/.ssh/id_rsa
```
