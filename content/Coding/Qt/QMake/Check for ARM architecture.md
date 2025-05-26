---
{"publish":true,"cssclasses":""}
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