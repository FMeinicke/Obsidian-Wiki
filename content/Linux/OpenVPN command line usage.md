---
{"publish":true,"cssclasses":""}
---


#openvpn/cli #vpn #apt/install 

> [!info] Source
> 
> - <https://askubuntu.com/a/898437/1152691>

- install openvpn (e.g. `sudo apt install openvpn`)
- copy/move the VPN config file to `/etc/openvpn/` and rename it, if necessary, to have a `.conf` extension
- start the connection using

```shell
sudo openvpn /etc/openvpn/<your-vpn-config.conf>
2024-07-30 11:32:39 OpenVPN 2.5.1 arm-unknown-linux-gnueabihf [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on May 14 2021
2024-07-30 11:32:39 library versions: OpenSSL 1.1.1n  15 Mar 2022, LZO 2.10
🔐 Enter Auth Username: your-vpn-user
🔐 Enter Auth Password: (no echo) # enter password
```