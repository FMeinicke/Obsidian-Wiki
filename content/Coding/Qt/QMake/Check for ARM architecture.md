---
publish: true
created: 2025-03-08T16:46:38.645+01:00
modified: 2025-05-26T17:03:05.000+02:00
published: 2025-05-26T17:03:05.000+02:00
---

#qmake/contains #qmake/QMAKE_HOST #raspberry #arm

> [!info] Source
>
> - <https://stackoverflow.com/a/39792865/12780516>
> - <https://stackoverflow.com/a/76532117/12780516>

```qmake
linux {
    # this only works if building *on* a raspi
    #contains(QMAKE_HOST.arch, arm.*):{
    # this also works if cross-building for a raspi
    contains(QMAKESPEC, .*linux-rasp-pi\d*-.*) {
        # code for raspis
    } else {
        # code for all other Linuxes
    }
}
```
