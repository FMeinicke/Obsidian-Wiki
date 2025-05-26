---
publish: true
sorting-spec: |-
  SSH
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [`ssh-agent` on Windows](SSH/`ssh-agent` on Windows.md)
- [How to use `Match` in ssh config](SSH/How to use `Match` in ssh config.md)
- [SSH tunneling to a host that is not directly reachable](SSH/SSH tunneling to a host that is not directly reachable.md)
- [Windows SSH Server PublicKey Login für Administratoren](SSH/Windows SSH Server PublicKey Login für Administratoren.md)

---


#ssh/config #ssh/key #admin #windows

> [!info] Source
>
> - <http://woshub.com/using-ssh-key-based-authentication-on-windows/>

- `C:\ProgramData\ssh\administrators_authorized_keys`
- `C:\ProgramData\ssh\sshd_config`
  - `PubkeyAuthentication yes`
  - `StrictModes no`


#ssh #ssh-agent #ssh-add #ssh/key #pwsh/set-service #pwsh/start-service #windows

> [!info] Source
>
>

```powershell
> Set-Service ssh-agent -StartupType Automatic
> Start-Service ssh-agent
```

Then add keys to the agent as usual with

```powershell
> ssh-add ~\.ssh\id_rsa
```


#ssh #ssh/config #tunneling #linux #windows

> [!info] Source
>
> - <https://www.tecmint.com/access-linux-server-using-a-jump-host/>

- Use `ssh -L [bind_address:]port:host:hostport jump-host` to connect to `jump-host` and forward the port `hostport` from the not-directly-reachable `host` to the local (client) `port` (if the optional `bind_address` is omitted, `port` will be available on all interfaces, otherwise only on the selected one)
- Then you can connect to the desired host with `ssh user@localhost -p port` (substituting `user` for the actual user name and `port` with the selected local `port` from the first command)

There is also the possibility to configure the jump host statically in the `.ssh/config` so that the connection to the remote server can be established using a single command.
Add the following to the `.ssh/config` (replacing `<IP_OR_HOSTNAME>` and `<USER_NAME>` with the appropriate values):

```conf
Host jump_host
  Hostname <IP_OR_HOSTNAME>
  User "<USER_NAME>"

Host remote_server
  Hostname <IP_OR_HOSTNAME>
  User <USER_NAME>
  ProxyJump jump_host
```

Now you can connect to the remote server with a simple

```shell
ssh -J jump_host remote_server
```

There is also another method that uses the `ProxyCommand` instead of the `ProxyJump` option. This is especially useful if the remote server is to be used with SSHFS-Win since it allows connecting to the remote server using just

```shell
ssh remote_server
```

Simply change the `ProxyJump` line from above to

```conf
ProxyCommand ssh -q -W %h:%p jump_host
```

- `-q` turns on quiet mode to suppress warnings and diagnostic messages
- `-W` requests that standard input and output on the client be forwarded to HOST on PORT over the secure channel
- `%h` specifies the host to connect to
- `%p` specifies the port to connect to on the remote host

> [!NOTE]
> Unfortunately, for this to work seamlessly with SSHFS-Win we need to follow [this](https://github.com/winfsp/sshfs-win/issues/166#issuecomment-1013741113) workaround (slightly modified):
>
> > A dirty solution:
> >
> > 1. Install busybox-w32 (`winget install busybox-w32`):
> > 2. Create a hardlink at `/path/to/SSHFS-Win/bin/sh.exe` that points to `/path/to/busybox.exe` (`busybox.exe` may be called something weird like `busybox-w64-FRP-5007-g82accfc19.exe`).
> >
> >    ```powershell
> >    cd "C:\Program Files\SSHFS-Win\bin"
> >    sudo New-Hardlink sh.exe '"$env:USERPROFILE\AppData\Local\Microsoft\WinGet\Packages\frippery.busybox-w32_Microsoft.Winget.Source_8wekyb3d8bbwe\busybox-w64-FRP-5007-g82accfc19.exe"'
> >    ```


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

---

## Tagged mentions


