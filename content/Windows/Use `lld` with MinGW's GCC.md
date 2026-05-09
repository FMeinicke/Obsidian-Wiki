---
publish: true
created: 2024-12-06T06:58:21.813+01:00
modified: 2025-05-27T08:42:51.000+02:00
published: 2025-05-27T08:42:51.000+02:00
---

#mingw #gcc #lld #llvm #linker #qmake #cmake

> [!info] Source

- with QMake ^dfbeda
  - add `QMAKE_LFLAGS*=-fuse-ld=lld` as additional qmake arguments or anywhere in a `.pro` or `.pri` file
- with CMake ^85c9b4
  - add `-DCMAKE_CXX_FLAGS="-fuse-ld=lld"` to the command line
  - add `list(APPEND CMAKE_CXX_FLAGS "-fuse-ld=lld")` in a `CMakeLists.txt` file
