---
publish: true
created: 2025-01-15T16:58:05.733+01:00
modified: 2025-05-26T17:03:29.000+02:00
published: 2025-05-26T17:03:29.000+02:00
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

- there's also the option to use existing metadata to overwrite other metadata, e.g., to set the _DateTimeOriginal_ from the file's modification time

```shell
exiftool "-DateTimeOriginal>FileModifyDate" test.jpg
```
