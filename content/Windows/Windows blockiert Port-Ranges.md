---
{"publish":true,"created":"2025-05-15T09:01:52.342+02:00","modified":"2025-05-27T08:42:35.107+02:00","published":"2025-05-27T08:42:35.107+02:00","cssclasses":""}
---

#grpc #sila #port #tcp #windows/netsh

> [!info] Source
>
> - <https://stackoverflow.com/questions/54010365/how-to-see-what-is-reserving-ephemeral-port-ranges-on-windows>

- To see the excluded port range

  ```powershell
  > netsh int ip show excludedportrange protocol=tcp

  Portausschlussbereiche für das Protokoll "tcp"

  Startport      Endport
  ----------    --------
        5357        5357
        5985        5985
       47001       47001
       49152       49152
       49153       49153
       49154       49154
       49851       49950
       50000       50059     *
       50060       50159
       50705       50804
       50805       50904
       50905       51004
       51005       51104
       60706       60805
       60806       60905

  * - Verwaltete Portausschlüsse.
  ```

- To free up some of these ports restart WinNAT service

  ```powershell
  > sudo net stop winnat
  > sudo net start winnat
  ```

- After this the excluded port range is reduces to the following for me

  ```powershell
  > netsh int ip show excludedportrange protocol=tcp

  Portausschlussbereiche für das Protokoll "tcp"

  Startport      Endport
  ----------    --------
        5357        5357
        5985        5985
       47001       47001
       49152       49152
       49153       49153
       49154       49154
       50000       50059     *

  * - Verwaltete Portausschlüsse.
  ```

This issue caused the error `Failed to bind to address 192.168.101.39:51064` (for example) with no further information on why the address could not be bound when attempting to start some SiLA Servers:

```log
2023-03-21 07:26:10,714 [MainThread  ] DEBUG   | sila_cetoni.application.application application.__start_servers (173): Starting SiLA 2 servers...
2023-03-21 07:26:10,717 [MainThread  ] INFO    | sila2.server.sila_server sila_server.__start (286): Starting SiLA server with encryption
E0321 07:26:10.720000000 23280 src/core/ext/transport/chttp2/server/secure/server_secure_chttp2.cc:120] {"created":"@1679379970.720000000","description":"No address added out of total 1 resolved","file":"src/core/ext/transport/chttp2/server/chttp2_server.cc","file_line":936,"referenced_errors":[{"created":"@1679379970.720000000","description":"Failed to add port to server","file":"src/core/lib/iomgr/tcp_server_windows.cc","file_line":509,"referenced_errors":[{"created":"@1679379970.720000000","description":"OS Error","file":"src/core/lib/iomgr/tcp_server_windows.cc","file_line":206,"os_error":"Unable to retrieve error string","syscall":"bind","wsa_error":10013}]}]}
2023-03-21 07:26:10,733 [MainThread  ] CRITICAL| sila_cetoni.application.application application.__start_servers (209): Failed to bind to address 192.168.101.39:51054; set GRPC_VERBOSITY=debug environment variable to see detailed error message.
Traceback (most recent call last):
  File "C:\CodingXP\cetoni_projects\sila_cetoni\sila_cetoni\application\sila_cetoni\application\application.py", line 194, in __start_servers
    server.start(
  File "C:\Users\Florian Meinicke\.virtualenvs\sila_cetoni_dev\lib\site-packages\sila2\server\sila_server.py", line 373, in start
    self.__start(
  File "C:\Users\Florian Meinicke\.virtualenvs\sila_cetoni_dev\lib\site-packages\sila2\server\sila_server.py", line 288, in __start
    self.grpc_server.add_secure_port(address_string, server_credentials=credentials)
  File "C:\Users\Florian Meinicke\.virtualenvs\sila_cetoni_dev\lib\site-packages\grpc\_server.py", line 973, in add_secure_port
    return _common.validate_port_binding_result(
  File "C:\Users\Florian Meinicke\.virtualenvs\sila_cetoni_dev\lib\site-packages\grpc\_common.py", line 166, in validate_port_binding_result
    raise RuntimeError(_ERROR_MESSAGE_PORT_BINDING_FAILED % address)
RuntimeError: Failed to bind to address 192.168.101.39:51054; set GRPC_VERBOSITY=debug environment variable to see detailed error message.
```

Resource Monitor also did not show any services or processes occupying this port.