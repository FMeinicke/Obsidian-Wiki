---
{"publish":true,"cssclasses":""}
---


#update-alternatives #editor #vim

> [!info] Source
> 
> - <https://askubuntu.com/a/891931/1152691>

```console
$ sudo update-alternatives --config editor
[sudo] password for user1:
There are 3 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path               Priority   Status
------------------------------------------------------------
* 0            /bin/nano           40        auto mode
  1            /bin/nano           40        manual mode
  2            /usr/bin/mcedit     25        manual mode
  3            /usr/bin/vim.tiny   15        manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
```

- note that if `vim` doesn't show up in this menu, it probably means that it points to `vim.tiny` (or `vim.basic`)

```console
$ ll $(which vim)
lrwxrwxrwx 1 root root 26 May  4  2023 /usr/bin/vim -> /etc/alternatives/vim.tiny*
```