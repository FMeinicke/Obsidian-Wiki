---
{"publish":true,"created":"2025-05-15T09:01:51.733+02:00","modified":"2025-05-27T08:42:33.747+02:00","published":"2025-05-27T08:42:33.747+02:00","cssclasses":""}
---

#hyper-v/switch #nat #pwsh

> [!info] Source
> 
> - <https://www.windowspro.de/wolfgang-sommergut/nat-switch-hyper-v-einrichten-windows-10-server-2016>

- neuen **"Internen"** Switch im Hyper-V-Manager anlegen
- Konfiguration danach nur über PowerShell möglich (**Admin-Rechte erforderlich!**)

```powershell
> Get-NetAdapter

Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
----                      --------------------                    ------- ------       ----------             ---------
VMware Network Adapte...8 VMware Virtual Ethernet Adapter for VM…      15 Up           00-50-56-C0-00-08       100 Mbps
vEthernet (Hyper-V NAT)   Hyper-V Virtual Ethernet Adapter #4          72 Up           00-15-5D-65-1B-03        10 Gbps
VMware Network Adapte...1 VMware Virtual Ethernet Adapter for VM…      12 Up           00-50-56-C0-00-01       100 Mbps
WLAN                      Edimax AC1200 MU-MIMO WiFi Nano USB 2.…       9 Disconnected 08-BE-AC-3B-C6-73          0 bps
Ethernet                  Realtek PCIe GbE Family Controller            6 Up           A8-A1-59-31-0F-FD         1 Gbps


> New-NetIPAddress -IPAddress 192.168.200.1 -PrefixLength 24 -InterfaceIndex 72

IPAddress         : 192.168.200.1
InterfaceIndex    : 72
InterfaceAlias    : vEthernet (Hyper-V NAT)
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 24
PrefixOrigin      : Manual
SuffixOrigin      : Manual
AddressState      : Tentative
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 192.168.200.1
InterfaceIndex    : 72
InterfaceAlias    : vEthernet (Hyper-V NAT)
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 24
PrefixOrigin      : Manual
SuffixOrigin      : Manual
AddressState      : Invalid
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : PersistentStore


> New-NetNat -Name "Hyper-V NAT" -InternalIPInterfaceAddressPrefix 192.168.200.0/24

Name                             : Hyper-V NAT
ExternalIPInterfaceAddressPrefix :
InternalIPInterfaceAddressPrefix : 192.168.200.0/24
IcmpQueryTimeout                 : 30
TcpEstablishedConnectionTimeout  : 1800
TcpTransientConnectionTimeout    : 120
TcpFilteringBehavior             : AddressDependentFiltering
UdpFilteringBehavior             : AddressDependentFiltering
UdpIdleSessionTimeout            : 120
UdpInboundRefresh                : False
Store                            : Local
Active                           : True
```

- danach in der VM eine IP-Adresse statisch konfigurieren (DHCP ist nicht automatisch möglich wie bei VMware; man könnte eine VM mit DHCP Server laufen lassen) --> z.B. IP: 192.168.200.2, Netmask: 255.255.255.0, Gateway: 192.168.200.1