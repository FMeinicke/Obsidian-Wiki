---
{"publish":true,"cssclasses":""}
---

#cmake/cmake_cxx_flags #big-obj

> [!info] Source
> 
> - <https://github.com/JuliaInterop/libcxxwrap-julia/issues/84>

- add the following to the command line call

```shell
-DCMAKE_CXX_FLAGS="-Wa,-mbig-obj"
```