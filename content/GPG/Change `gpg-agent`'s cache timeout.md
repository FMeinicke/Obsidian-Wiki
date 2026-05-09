---
publish: true
created: 2024-12-06T06:58:20.627+01:00
modified: 2025-05-26T17:03:19.000+02:00
published: 2025-05-26T17:03:19.000+02:00
---

#gpg-agent #gpg/cache-ttl #gpgconf

> [!info] Source
>
> - <https://superuser.com/a/1428651>

Create/edit `$env:Appata/gnupg/gpg-agent.conf` (could also be `~/.gnupg/gpg-agent.conf`) and add/change the following lines:

```conf
# default-cache-ttl
#   Set the time a cache entry is valid to n seconds. The default is 600
#   seconds. Each time a cache entry is accessed, the entry’s timer is reset. To
#   set an entry’s maximum lifetime, use max-cache-ttl.
# 365 days
default-cache-ttl 78840000

# max-cache-ttl
#   Set the maximum time a cache entry is valid to n seconds. After this time a
#   cache entry will be expired even if it has been accessed recently or has
#   been set using gpg-preset-passphrase. The default is 2 hours (7200 seconds).
# 365 days
max-cache-ttl 78840000

```

This example sets the cache timeout to 1 year. The values are specified as seconds.

Then reload the agent and verify that the changes have been applied:

```shell
> gpgconf --reload gpg-agent
> gpgconf --list-options gpg-agent
...
default-cache-ttl:24:0:Lösche unbenutzte Passwörter nach N Sekunden aus dem Cache:3:3:N:600::78840000
default-cache-ttl-ssh:24:1:Lösche unbenutzte SSH Passwörter nach N Sekunden aus dem Cache:3:3:N:1800::
max-cache-ttl:24:2:Lösche Passwörter nach N Sekunden aus dem Cache:3:3:N:7200::78840000
max-cache-ttl-ssh:24:2:Lösche SSH Passwörter nach N Sekunden aus dem Cache:3:3:N:7200::
...
```
