---
{"publish":true,"cssclasses":"hide_properties"}
---


- [`date` milliseconds since epoch](Linux/Commands/`date` milliseconds since epoch.md)
- [ls with path](Linux/Commands/ls with path.md)
- [rsync with identity file](Linux/Commands/rsync with identity file.md)
- [wget without checking server certificate](Linux/Commands/wget without checking server certificate.md)
- [awk](awk)
    - [Count from the end](Linux/Commands/awk/Count from the end.md)
- [find](find)
    - [`chmod` all files or directories recursively](Linux/Commands/find/`chmod` all files or directories recursively.md)
    - [Find hardlinks](Linux/Commands/find/Find hardlinks.md)
    - [Use `bash -c` in `-exec`](Linux/Commands/find/Use `bash -c` in `-exec`.md)
- [grep](grep)
    - [Fix grep binary file matches](Linux/Commands/grep/Fix grep binary file matches.md)
    - [Match exactly](Linux/Commands/grep/Match exactly.md)
- [openssl](openssl)
    - [Generate a random string](Linux/Commands/openssl/Generate a random string.md)
    - [Generate AES key](Linux/Commands/openssl/Generate AES key.md)
- [sed](sed)
    - [Comment and uncomment lines](Linux/Commands/sed/Comment and uncomment lines.md)
    - [Multiple commands](Linux/Commands/sed/Multiple commands.md)
    - [Using different delimiters](Linux/Commands/sed/Using different delimiters.md)
- [vim](vim)
    - [Paste in insert mode](Linux/Commands/vim/Paste in insert mode.md)
    - [replace all occurrences](Linux/Commands/vim/replace all occurrences.md)
    - [Replace with a newline](Linux/Commands/vim/Replace with a newline.md)

---



#wget/no-check-certificate

> [!info] Source
> 
> - `man wget`

```shell
wget --no-check-certificate ...
```




#rsync/-e #rsync/--rsh

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/127355/482223>

- use the `--rsh=COMMAND`/`-e` flag
```shell
rsync -e "ssh -i ~/.ssh/id_rsa" ...
```




#ls/-1

> [!info] Source
> 
> - <https://stackoverflow.com/a/3572628/12780516>

```console
$ ls -1 $PWD/**
/workspaces/cetoni_ui/CHANGELOG.md
/workspaces/cetoni_ui/Dockerfile
/workspaces/cetoni_ui/README.md
/workspaces/cetoni_ui/pyproject.toml
/workspaces/cetoni_ui/uv.lock

/workspaces/cetoni_ui/src:
cetoni_ui

# or

$ ls .git/hooks/**
.git/hooks/applypatch-msg.sample
.git/hooks/commit-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/post-checkout
.git/hooks/post-merge
.git/hooks/post-rewrite
.git/hooks/post-update.sample
.git/hooks/pre-applypatch.sample
.git/hooks/pre-commit
.git/hooks/pre-commit.sample
.git/hooks/pre-merge-commit.sample
.git/hooks/pre-push
.git/hooks/pre-push.sample
.git/hooks/pre-rebase.sample
.git/hooks/pre-receive.sample
.git/hooks/prepare-commit-msg.sample
.git/hooks/push-to-checkout.sample
.git/hooks/sendemail-validate.sample
.git/hooks/update.sample
```


[[`date` milliseconds since epoch]]

---

## Tagged mentions


