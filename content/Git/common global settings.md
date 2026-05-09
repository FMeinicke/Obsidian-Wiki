---
publish: true
created: 2024-12-06T06:58:23.803+01:00
modified: 2025-05-26T17:03:51.000+02:00
published: 2025-05-26T17:03:51.000+02:00
---

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
