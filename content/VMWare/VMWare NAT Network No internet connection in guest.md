---
publish: true
title: "VMWare NAT Network: No internet connection in guest"
created: 2025-05-15T09:01:51.483+02:00
modified: 2025-05-27T08:42:17.876+02:00
published: 2025-05-27T08:42:17.876+02:00
cssclasses: ""
---


#vmware/nat #linux/dhclient #dhcp

> [!info] Source
> 
> - <https://community.broadcom.com/vmware-cloud-foundation/discussion/vmware-176-nat-network-connection-drops-on-windows-11-23h2-host-machine>

- try restarting the *VMWare NAT service* while the client (VMWare or the guest VM?) is running
- try acquiring a new DHCP lease in the guest (`sudo dhclient` on Linux)
