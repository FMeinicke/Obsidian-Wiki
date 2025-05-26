---
{"publish":true,"cssclasses":"hide_properties"}
---


- [Finding Boost with MinGW on Windows](Coding/CMake/Finding Boost with MinGW on Windows.md)
- [Fix 'file too big' error](Coding/CMake/Fix 'file too big' error.md)
- [Use `lld`](Coding/CMake/Use `lld`.md)


#mingw #windows #boost

> [!info] Source
>
> - <https://gitlab.kitware.com/cmake/cmake/-/issues/22968>


#cmake/cmake_cxx_flags #big-obj

> [!info] Source
> 
> - <https://github.com/JuliaInterop/libcxxwrap-julia/issues/84>

- add the following to the command line call

```shell
-DCMAKE_CXX_FLAGS="-Wa,-mbig-obj"
```


#cmake/cmake_cxx_flags #cmake/cmakelists #lld

---
sorting-spec: |-
  Windows
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Change swap file (pagefile.sys) size](Windows/Change swap file \(pagefile.sys\) size.md)
    
- [Custom Shortcuts](Windows/Custom Shortcuts.md)
    
- [Disable side-channel mitigations in VMWare Workstation Player](Windows/Disable side-channel mitigations in VMWare Workstation Player.md)
    
- [Find out which process uses a specific port](Windows/Find out which process uses a specific port.md)
    
- [Hibernate from the command line](Windows/Hibernate from the command line.md)
    
- [Use `lld` with MinGW's GCC](Windows/Use `lld` with MinGW's GCC.md)
    
- [Windows blockiert Port-Ranges](Windows/Windows blockiert Port-Ranges.md)
    
- [Hyper-V](Hyper-V)
    
    - [Change display resolution](Windows/Hyper-V/Change display resolution.md)
        
    - [NAT Switch à la VMware](Windows/Hyper-V/NAT Switch à la VMware.md)
        
    - [Excel](Excel)
        
        - [Compare cell value with text for conditional formatting](Windows/Office/Excel/Compare cell value with text for conditional formatting.md)
        - [Format floating point numbers from 0 - 100 as percentages](Windows/Office/Excel/Format floating point numbers from 0 - 100 as percentages.md)
        - [Format numbers as file sizes](Windows/Office/Excel/Format numbers as file sizes.md)
    - [PowerPoint](PowerPoint)
        
    - [Word](Word)
        
- [Powershell](Powershell)
    
    - [`foreach`](Windows/Powershell/`foreach`.md)
    - [Arrays](Windows/Powershell/Arrays.md)
    - [Bash brace-expansion equivalent](Windows/Powershell/Bash brace-expansion equivalent.md)
    - [Command-Output to Clipboard](Windows/Powershell/Command-Output to Clipboard.md)
    - [Difference between ampersand (`&`) and dot (`.`)](Windows/Powershell/Difference between ampersand \(`&`\) and dot \(`.`\).md)
    - [Don't fail if removing non-existent items](Windows/Powershell/Don't fail if removing non-existent items.md)
    - [Enter a Visual Studio dev shell](Windows/Powershell/Enter a Visual Studio dev shell.md)
    - [Escape double quotes](Windows/Powershell/Escape double quotes.md)
    - [List all environment variables](Windows/Powershell/List all environment variables.md)
    - [Print environment variable of process](Windows/Powershell/Print environment variable of process.md)
    - [Unix `curl` equivalent](Windows/Powershell/Unix `curl` equivalent.md)
    - [Unix `cut` equivalent](Windows/Powershell/Unix `cut` equivalent.md)
    - [Unix `find` equivalent](Windows/Powershell/Unix `find` equivalent.md)
    - [Unix `grep` equivalent](Windows/Powershell/Unix `grep` equivalent.md)
    - [Unix `read` equivalent](Windows/Powershell/Unix `read` equivalent.md)
    - [Unix `touch` equivalent](Windows/Powershell/Unix `touch` equivalent.md)

---

#windows/shortcuts #windows/powertoys

> [!info] Source
> 
> - 

| Shortcut                                                                                                                                                                           | Description                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>                                                                                                                                       | PowerToys: Extended Insert         |
| <kbd>Win</kbd>+<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd>                                                                                                                         | PowerToys: Insert as Text-only     |
| <kbd>Win</kbd>+<kbd>Ctrl</kbd>+<kbd>T</kbd>                                                                                                                                        | PowerToys: Window Always On Top    |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd>                                                                                                                                       | PowerToys: Color Picker            |
| <kbd>Win</kbd>+<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>                                                                                                                       | PowerToys: Crop and Lock Thumbnail |
| <kbd>Win</kbd>+<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>                                                                                                                       | PowerToys: Crop and Lock Reparent  |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>Ö</kbd>                                                                                                                                       | PowerToys: FancyZones Editor       |
| <kbd>Ctrl</kbd>+<kbd>Ctrl</kbd>                                                                                                                                                    | PowerToys: Find My Mouse           |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>                                                                                                                                        | PowerToys: Mouse Crosshair         |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd>                                                                                                                                       | PowerToys: Mouse Marker            |
| <kbd>Win</kbd>+<kbd>Space</kbd>                                                                                                                                                    | PowerToys: PowerToys Run           |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>                                                                                                                                       | PowerToys: On Screen Ruler         |
| <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>                                                                                                                                       | PowerToys: Text Extractor          |
| <kbd>\<Key to add an accent to\></kbd>+<kbd>Space</kbd> or<br><kbd>\<Key to add an accent to\></kbd>+<kbd>Left</kbd> or<br><kbd>\<Key to add an accent to\></kbd>+<kbd>Right</kbd> | PowerToys: Quick Accent            |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>                                                                                                                                        | Launch Terminal                    |

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

#port #pwsh/get-process #pwsh/get-nettcpconnection #pwsh/get-netudpendpoint #tcp #udp

> [!info] Source
>
> - <https://stackoverflow.com/a/48199/12780516>

- for TCP connections

  ```powershell
  Get-Process -Id (Get-NetTCPConnection -LocalPort <PORT>).OwningProcess
  ```

- for UDP connections

  ```powershell
  Get-Process -Id (Get-NetUDPEndpoint -LocalPort <PORT>).OwningProcess
  ```

#mingw #gcc #lld #llvm #linker #qmake #cmake

> [!info] Source
>
>

- with QMake ^dfbeda
  - add `QMAKE_LFLAGS*=-fuse-ld=lld` as additional qmake arguments or anywhere in a `.pro` or `.pri` file
- with CMake ^85c9b4
  - add `-DCMAKE_CXX_FLAGS="-fuse-ld=lld"` to the command line
  - add `list(APPEND CMAKE_CXX_FLAGS "-fuse-ld=lld")` in a `CMakeLists.txt` file

#vmware/vmx #side-channel-mitigations

> [!info] Source
> 
> - <https://www.reddit.com/r/vmware/comments/j2fyfl/comment/g87z5y5/>

- add the following to the VM's `.vmx` file

```ini
ulm.disableMitigations = "TRUE"
```

#windows/shutdown/h #hibernate

> [!info] Source
> 
> - <https://www.tenforums.com/general-support/94012-sleep-hibernate-command-line-post1149228.html?s=c48ddb4ee015890da185a0be3c8729e4#post1149228>

```shell
shutdown /h
```

#windows/pagefile #windows/swap #swap #ram

> [!info] Source
> 
> - <https://superuser.com/a/793325/1201131>

- press <kbd>Win</kbd>+<kbd>R</kbd> to bring up the command runner and enter `systempropertiesadvanced.exe`, then press <kbd>Enter</kbd>
- in the dialog that opened go to the **Advanced** tab, then under *Performance* click *Settings...*
- in the next dialog go to the **Advanced** tab again, and under *Virtual Memory* click *Change...*
- in that dialog select a drive for where to store the swap file (you can have multiple files on different drives) and enter the desired minimum and maximum sizes, or let Windows decide
- when you're done, click *Set*, then *OK*, followed by two more *OK*s for the other two dialogs to close everything

---



---

## Tagged mentions




---

## Tagged mentions


