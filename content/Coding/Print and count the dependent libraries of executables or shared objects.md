---
publish: true
created: 2025-03-08T16:46:36.575+01:00
modified: 2025-05-26T17:02:14.000+02:00
published: 2025-05-26T17:02:14.000+02:00
---

#linux #objdump/-p #grep #awk #sort/-n #uniq/-c

> [!info] Source
>
> - <https://stackoverflow.com/a/15520982/12780516>
> - <https://stackoverflow.com/a/50218/12780516>

```shell
objdump -p /usr/local/lib/libmylibs*.so | grep NEEDED | awk '{ print $2 }' | sort | uniq -c | sort -n
      1 libboost_locale.so.1.74.0
      1 libcsi.so.1
      1 libicui18n.so.72
      1 libicuuc.so.72
      1 liblabbcan_canopen.so.1
      1 liblabbcan_local.so.1
      1 libpython3.10.so.1.0
      1 libqstatemachineex.so.1
      1 libserial.so.1
      1 libsocketcan.so.2
      1 libspize.so.1
      2 libQt6StateMachine.so.6
      2 libboost_thread.so.1.74.0
      2 libcanoo.so.1
      2 liblabbcan_sim.so.1
      2 libqtcoreaddons.so.1
      2 libunits.so
      3 ld-linux-x86-64.so.2
      4 liblabbcan_device.so.1
      5 libboost_filesystem.so.1.74.0
      5 liblabbcan_core.so.1
      6 liblabbcan_common.so.1
      8 libm.so.6
     12 libusl.so.1
     13 libQt6Core.so.6
     13 liblog4cplus-2.0.so.3
     22 libgcc_s.so.1
     22 libstdc++.so.6
     23 libc.so.6
```

---
