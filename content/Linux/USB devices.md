---
{"publish":true,"cssclasses":""}
---


#usb #devices #udev #udevadm #ftdi

> [!info] Source
>
> - <https://unix.stackexchange.com/a/183492>
> - <https://unix.stackexchange.com/a/144735>
> - <http://www.reactivated.net/writing_udev_rules.html#example-printer>

- basic info about connected devices

  ```shell
  $ lsusb
  Bus 001 Device 012: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 010: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 007: ID 0424:ec00 Microchip Technology, Inc. (formerly SMSC) SMSC9512/9514 Fast Ethernet Adapter
  Bus 001 Device 005: ID 0424:9512 Microchip Technology, Inc. (formerly SMSC) SMC9512/9514 USB Hub
  Bus 001 Device 017: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 016: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 015: ID 1a40:0201 Terminus Technology Inc. FE 2.1 7-port Hub
  Bus 001 Device 014: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 013: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 011: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 009: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 008: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 006: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
  Bus 001 Device 004: ID 1a40:0201 Terminus Technology Inc. FE 2.1 7-port Hub
  Bus 001 Device 003: ID 0424:ec00 Microchip Technology, Inc. (formerly SMSC) SMSC9512/9514 Fast Ethernet Adapter
  Bus 001 Device 002: ID 0424:9514 Microchip Technology, Inc. (formerly SMSC) SMC9514 Hub
  Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
  ```

- tree view of connected devices

  ```shell
  $ lsusb -t
  /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=dwc2/1p, 480M
      |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/5p, 480M
          |__ Port 1: Dev 3, If 0, Class=Vendor Specific Class, Driver=smsc95xx, 480M
          |__ Port 2: Dev 4, If 0, Class=Hub, Driver=hub/7p, 480M
              |__ Port 7: Dev 15, If 0, Class=Hub, Driver=hub/7p, 480M
                  |__ Port 1: Dev 16, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
                  |__ Port 2: Dev 17, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 5: Dev 13, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 3: Dev 9, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 1: Dev 6, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 6: Dev 14, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 4: Dev 11, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 2: Dev 8, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
          |__ Port 5: Dev 5, If 0, Class=Hub, Driver=hub/3p, 480M
              |__ Port 1: Dev 7, If 0, Class=Vendor Specific Class, Driver=smsc95xx, 480M
              |__ Port 2: Dev 10, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
              |__ Port 3: Dev 12, If 0, Class=Vendor Specific Class, Driver=ftdi_sio, 12M
  ```

- get some more-than-basic info

  ```shell
  $ usb-devices

  T:  Bus=01 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=480 MxCh= 3
  D:  Ver= 2.00 Cls=09(hub  ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
  P:  Vendor=1d6b ProdID=0002 Rev=04.04
  S:  Manufacturer=Linux 4.4.0-131-generic ehci_hcd
  S:  Product=EHCI Host Controller
  S:  SerialNumber=0000:00:1a.0
  C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
  I:  If#= 0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub
  ```

- get very detailed info (useful for writing udev rules)

  ```shell
  udevadm info --name=/dev/ttyUSB0 --attribute-walk
  ```

- using that info you can create a udev rule, e.g. to create a `/dev/your_device_name` device that will always be symlinked to the corresponding `/dev/ttyUSBx` device for that physical USB device

  ```
  SUBSYSTEM=="tty", ATTRS{idVendor}=="1234", ATTRS{idProduct}=="5678", SYMLINK+="your_device_name"
  ```

- reload udev rules using

  ```shell
  sudo udevadm control --reload-rules  # or --reload
  ```

- then trigger the rule using

  ```shell
  sudo udevadm trigger
  ```