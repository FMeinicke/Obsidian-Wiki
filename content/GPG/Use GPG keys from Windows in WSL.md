---
publish: true
created: 2024-12-06T06:58:21.154+01:00
modified: 2025-06-04T11:20:23.000+02:00
published: 2025-06-04T11:20:23.000+02:00
---

#gpg/pinentry #windows

> [!info] Source

- Install `gpg`
- [[GPG#Import a key|Import the GPG private key from Windows in WSL]] and trust it _ultimately_
- configure the WSL `gpg-agent` to use the Windows pinentry program for entering the passphrase --> create/edit `~/.gnupg/gpg-agent.conf` to contain

  ```shell
  # default-cache-ttl
  #   Set the time a cache entry is valid to n seconds. The default is 600
  #   seconds. Each time a cache entry is accessed, the entry’s timer is reset. To
  #   set an entry’s maximum lifetime, use max-cache-ttl.
  # 365 days
  default-cache-ttl 78840000

  # max-cache-ttl
  #   Set the maximum time a cache entry is valid to n seconds. After this time a
  #   cache entry will be expired even if it has been accessed recently or has
  #   been set using gpg-preset-passphrase. The default is 2 hours (7200 seconds).
  # 365 days
  max-cache-ttl 78840000

  pinentry-program /mnt/c/Program Files (x86)/Gpg4win/bin/pinentry.exe
  ```

![[common global settings]]
