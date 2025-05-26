---
{"publish":true,"cssclasses":"hide_properties"}
---


- [Print and count the dependent libraries of executables or shared objects](Coding/Print and count the dependent libraries of executables or shared objects.md)
- [Specify number of parallel processes for jom](Coding/Specify number of parallel processes for jom.md)
- [CMake](Coding/CMake)
    - [Finding Boost with MinGW on Windows](Coding/CMake/Finding Boost with MinGW on Windows.md)
    - [Fix 'file too big' error](Coding/CMake/Fix 'file too big' error.md)
    - [Use `lld`](Coding/CMake/Use `lld`.md)
- [HTML, CSS & friends](Coding/HTML, CSS & friends)
    - [Hide element but keep space](Coding/HTML, CSS & friends/Hide element but keep space.md)
    - [Ordered list with circled numbers](Coding/HTML, CSS & friends/Ordered list with circled numbers.md)
- [JavaScript](Coding/JavaScript)
    - [Test if a string matches a regex](Coding/JavaScript/Test if a string matches a regex.md)
- [Python](Coding/Python)
    - [`Iterable` vs. `Sequence`](Coding/Python/`Iterable` vs. `Sequence`.md)
    - [abstract property](Coding/Python/abstract property.md)
    - [abstract static property](Coding/Python/abstract static property.md)
    - [Access `dist-packages` when inside a venv](Coding/Python/Access `dist-packages` when inside a venv.md)
    - [Check if type is built-in](Coding/Python/Check if type is built-in.md)
    - [Coding Guidelines](Coding/Python/Coding Guidelines.md)
    - [Difference between slash and asterisk in function parameter list](Coding/Python/Difference between slash and asterisk in function parameter list.md)
    - [Dynamically add property to a class](Coding/Python/Dynamically add property to a class.md)
    - [Find the path to actual installation directory for the Windows Store version](Coding/Python/Find the path to actual installation directory for the Windows Store version.md)
    - [Function decorator that accepts optional keyword-argument](Coding/Python/Function decorator that accepts optional keyword-argument.md)
    - [Get class of a generic class's `TypeVar`](Coding/Python/Get class of a generic class's `TypeVar`.md)
    - [Get the number of parameters for a function](Coding/Python/Get the number of parameters for a function.md)
    - [How to use `Q_ARG` and `Q_RETURN_ARG` with `QMetaObject.invokeMethod()` in PySide6](Coding/Python/How to use `Q_ARG` and `Q_RETURN_ARG` with `QMetaObject.invokeMethod\(\)` in PySide6.md)
    - [Mock an `ImportError` with pytest](Coding/Python/Mock an `ImportError` with pytest.md)
    - [Proper Ctrl+C behavior with PySide2](Coding/Python/Proper Ctrl+C behavior with PySide2.md)
    - [stub generation](Coding/Python/stub generation.md)
- [Qt](Coding/Qt)
    - [Moving an object to a different thread](Coding/Qt/Moving an object to a different thread.md)
    - [QMake](Coding/Qt/QMake)
        - [Check for ARM architecture](Coding/Qt/QMake/Check for ARM architecture.md)
        - [Literal dollar sign](Coding/Qt/QMake/Literal dollar sign.md)
        - [Proper quoting and path separators](Coding/Qt/QMake/Proper quoting and path separators.md)
        - [Use `lld`](Coding/Qt/QMake/Use `lld`.md)

---


#jom

> [!info] Source
> 
> - `jom /?`

```pwsh
jom.exe /J 10 ...
```


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


---

## Tagged mentions


