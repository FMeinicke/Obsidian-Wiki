---
{"publish":true,"cssclasses":""}
---

#qmake/qmake_lflags #lld


#mingw #gcc #lld #llvm #linker #qmake #cmake

> [!info] Source
>
>

- with QMake ^dfbeda
  - add `QMAKE_LFLAGS*=-fuse-ld=lld` as additional qmake arguments or anywhere in a `.pro` or `.pri` file
- with CMake ^85c9b4
  - add `-DCMAKE_CXX_FLAGS="-fuse-ld=lld"` to the command line
  - add `list(APPEND CMAKE_CXX_FLAGS "-fuse-ld=lld")` in a `CMakeLists.txt` file