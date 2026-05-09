---
publish: true
created: 2025-03-08T16:46:38.998+01:00
modified: 2025-05-26T17:03:23.000+02:00
published: 2025-05-26T17:03:23.000+02:00
---

#cmake/cmake_cxx_flags #big-obj

> [!info] Source
>
> - <https://github.com/JuliaInterop/libcxxwrap-julia/issues/84>

- add the following to the command line call

```shell
-DCMAKE_CXX_FLAGS="-Wa,-mbig-obj"
```
