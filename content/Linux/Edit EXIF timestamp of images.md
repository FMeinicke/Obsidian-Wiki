---
publish: true
created: 2025-05-15T09:01:50.201+02:00
modified: 2025-05-26T15:25:10.106+02:00
published: 2025-05-26T15:25:10.106+02:00
cssclasses: ""
---


#linux/exiftool #image

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/217003/482223>
> - <https://unix.stackexchange.com/a/238528/482223>

```shell
exiftool -DateTimeOriginal="2023:10:2 10:01:50+02:00" IMG_20231002_100150605.JPG
```

- creation time: `-CreateDate`
- modification time: `-ModifyDate`
---
- there's also the option to use existing metadata to overwrite other metadata, e.g., to set the *DateTimeOriginal* from the file's modification time

```shell
exiftool "-DateTimeOriginal>FileModifyDate" test.jpg
```
