---
{"publish":true,"created":"2025-05-15T09:01:46.248+02:00","modified":"2025-05-26T15:25:01.199+02:00","published":"2025-05-26T15:25:01.199+02:00","cssclasses":""}
---

#cmake/cmake_cxx_flags #big-obj

> [!info] Source
> 
> - <https://github.com/JuliaInterop/libcxxwrap-julia/issues/84>

- add the following to the command line call

```shell
-DCMAKE_CXX_FLAGS="-Wa,-mbig-obj"
```