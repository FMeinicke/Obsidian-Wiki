---
publish: true
created: 2025-05-15T09:01:47.560+02:00
modified: 2025-06-04T11:20:13.582+02:00
published: 2025-06-04T11:20:13.582+02:00
cssclasses: ""
---

#gpg/pinentry #windows

> [!info] Source
>
>

- Install `gpg`
- [[GPG/GPG#Import a key\|Import the GPG private key from Windows in WSL]] and trust it *ultimately*
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


#git-config

> [!info] Source
>
> - <https://blog.gitbutler.com/how-git-core-devs-configure-git> (partly)

```ini
[core]
    autocrlf = true
    editor = code --wait
    # or for terminal-only
    #editor = vim
[user]
    name = Florian Meinicke
    email = florian.meinicke@cetoni.de
    signingKey = 6CA69321
[pull]
    rebase = true
[rebase]
    autoStash = true
    autoSquash = true
[init]
    defaultbranch = main
[commit]
    gpgSign = true
[tag]
    gpgSign = true
```

### Windows-specific

```ini
[core]
    # enable symlinks on Windows
    symlinks = true
    # use the Windows built-in ssh command instead of git's
    sshCommand = C:/Windows/System32/OpenSSH/ssh.exe
[credential]
    helper = manager-core
[gpg]
    program = C:\\Program Files (x86)\\Gpg4win\\..\\GnuPG\\bin\\gpg.exe
[http]
    # to allow connecting to servers via HTTPS w/ a self-signed certificate (Windows only)
    sslBackend = schannel
```

## Settings that even Git core developers change

```ini
# clearly makes git better

[column]
    ui = auto
[branch]
    sort = -committerdate
[tag]
    sort = version:refname
[init]
    defaultBranch = main
[diff]
    algorithm = histogram
    colorMoved = plain
    mnemonicPrefix = true
    renames = true
[push]
    default = simple
    autoSetupRemote = true
    followTags = true
[fetch]
    prune = true
    pruneTags = true
    all = true

# why the hell not?

[help]
    autocorrect = prompt
[commit]
    verbose = true
[rerere]
    enabled = true
    autoupdate = true
[core]
    excludesfile = ~/.gitignore
[rebase]
    autoSquash = true
    autoStash = true
    updateRefs = true

# a matter of taste (uncomment if you dare)

[core]
    # fsmonitor = true
    # untrackedCache = true
[merge]
    # (just 'diff3' if git version < 2.3)
    # conflictstyle = zdiff3 
[pull]
    # rebase = true
```
