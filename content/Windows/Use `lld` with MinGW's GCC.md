---
{"publish":true,"created":"2025-05-15T09:01:52.311+02:00","modified":"2025-05-27T08:42:35.060+02:00","published":"2025-05-27T08:42:35.060+02:00","cssclasses":""}
---

#mingw #gcc #lld #llvm #linker #qmake #cmake

> [!info] Source
>
>

- with QMake ^dfbeda
  - add `QMAKE_LFLAGS*=-fuse-ld=lld` as additional qmake arguments or anywhere in a `.pro` or `.pri` file
- with CMake ^85c9b4
  - add `-DCMAKE_CXX_FLAGS="-fuse-ld=lld"` to the command line
  - add `list(APPEND CMAKE_CXX_FLAGS "-fuse-ld=lld")` in a `CMakeLists.txt` file