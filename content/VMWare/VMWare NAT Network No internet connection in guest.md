---
{"publish":true,"title":"VMWare NAT Network: No internet connection in guest","cssclasses":""}
---


#vmware/nat #linux/dhclient #dhcp

> [!info] Source
> 
> - <https://community.broadcom.com/vmware-cloud-foundation/discussion/vmware-176-nat-network-connection-drops-on-windows-11-23h2-host-machine>

- try restarting the *VMWare NAT service* while the client (VMWare or the guest VM?) is running
- try acquiring a new DHCP lease in the guest (`sudo dhclient` on Linux)
