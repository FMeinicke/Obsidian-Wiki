---
{"publish":true,"cssclasses":""}
---


#vpn/wireguard #fritzbox #wg #wg-quick #systemctl 

> [!info] Source
> 
> - <https://wiki.ubuntuusers.de/WireGuard/> (for some basic concepts and commands)

- create the WireGuard VPN configuration on the server (in this case a FRITZ!Box) -> this yields a `wg_config.conf` file with the following content
  
  ```conf
  [Interface]
  PrivateKey = KPRaRgBEKgUQaNLKhjVVDNP5Pqf5CBDY3/FHWvDhwF4=
  Address = 192.168.0.209/24,fd69:2dc5:8de4::209/64
  DNS = 192.168.0.254,192.168.0.1,fe80::2a0:98ff:fe02:13f3,fd69:2dc5:8de4::e72:74ff:fe5b:45bf
  DNS = fritz.box
  
  [Peer]
  PublicKey = Z/fkUwCqxYCzgEaOU/Y8X9a0je82oT7gKO86skxaaAY=
  PresharedKey = mEwJ/N2oD9mfKTWmb/pggYY0MQ1/ob7Xz8VPtuX1pkI=
  AllowedIPs = 192.168.0.0/24,0.0.0.0/0,fd69:2dc5:8de4::/64,::/0
  Endpoint = xxxxxxxxxxxxxxxx.myfritz.net:12345
  PersistentKeepalive = 25
  ```

- on the WireGuard client, install `wireguard` and load the necessary kernel module
  
  ```console
  # apt install wireguard
  # modprobe wireguard
  # lsmod | grep wireguard
  wireguard             114688  0
  curve25519_x86_64      36864  1 wireguard
  libchacha20poly1305    16384  1 wireguard
  ip6_udp_tunnel         16384  1 wireguard
  udp_tunnel             32768  1 wireguard
  libcurve25519_generic    49152  2 curve25519_x86_64,wireguard
  ```

- create the client configuration file in the directory `/etc/wireguard/`, name it something like `wg0.conf`, and copy-and-paste the content from the file above

> [!attention] Important
> The FRITZ!Box generates a config file that routes all traffic through the WireGuard interface. However, we still want to be able to access the client (a publicly hosted Ubuntu VPS in this case) as before.  
> For this to work, we need to remove the `0.0.0.0/0,` and `,::/0` from the line `AllowedIPs` in the `[Peer]` section of the config file.

  the config file on the WireGuard client should now look like the following:
  
  ```conf
  [Interface]
  PrivateKey = KPRaRgBEKgUQaNLKhjVVDNP5Pqf5CBDY3/FHWvDhwF4=
  Address = 192.168.0.209/24,fd69:2dc5:8de4::209/64
  DNS = 192.168.0.254,192.168.0.1,fe80::2a0:98ff:fe02:13f3,fd69:2dc5:8de4::e72:74ff:fe5b:45bf
  DNS = fritz.box
  
  [Peer]
  PublicKey = Z/fkUwCqxYCzgEaOU/Y8X9a0je82oT7gKO86skxaaAY=
  PresharedKey = mEwJ/N2oD9mfKTWmb/pggYY0MQ1/ob7Xz8VPtuX1pkI=
  AllowedIPs = 192.168.0.0/24,fd69:2dc5:8de4::/64
  Endpoint = xxxxxxxxxxxxxxxx.myfritz.net:12345
  PersistentKeepalive = 25
  ```

- now, we can start, stop, and restart the connection using either `wg-quick` or `systemctl`
  
  ```console
  # wg-quick up wg0
  # wg-quick down wg0
  OR
  # systemctl start wg-quick@wg0
  # systemctl stop wg-quick@wg0
  # systemctl restart wg-quick@wg0
  ```

- using `wg show` you can show the current configuration and connection status, and `wg showconf wg0` shows the configuration of the interface (essentially the contents of the `/etc/wireguard/wg0.conf` file)
- to have the connection be activated automatically at boot, we can leverage `systemctl`:
  
  ```console
  # systemctl enable wg-quick@wg0.conf
  Created symlink /etc/systemd/system/multi-user.target.wants/wg-quick@VPN.service → /usr/lib/systemd/system/wg-quick@.service.
  ```

> [!hint]
> If `wg-quick up ...` or `systemctl start wg-quick@...` errs with the message `wg-quick: '...' already exists`, you need to delete the corresponding interface with `wg-quick down ...`. This was a problem when following the steps in the linked guide, as it describes that the interface needs to be created manually using `ip link add`, whereas this isn't actually necessary since this is done by `wg-quick up ...` automatically.
