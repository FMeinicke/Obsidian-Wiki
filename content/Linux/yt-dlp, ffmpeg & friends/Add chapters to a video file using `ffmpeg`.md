---
publish: true
created: 2024-12-06T06:58:10.707+01:00
modified: 2025-05-26T17:02:18.000+02:00
published: 2025-05-26T17:02:18.000+02:00
---

#ffmpeg

> [!info] Source(s)
>
> - <https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg>

- get the original metadata from the video file

```shell
ffmpeg -i INPUT.mp4 -f ffmetadata ffmetadata.txt
```

```ini
;FFMETADATA1
major_brand=isom
minor_version=512
compatible_brands=isomiso2avc1mp41
encoder=Lavf60.16.100
```

- add chapters to the metadata file
  - when using `TIMEBASE=1/1000`, the `START` and `END` values have to be in milliseconds, i.e. a timestamp of 2:32:13 would translate to 9133000

> [!example]-
>
> ```ini
> ;FFMETADATA1
> major_brand=isom
> minor_version=512
> compatible_brands=isomiso2avc1mp41
> encoder=Lavf60.16.100
>
> [CHAPTER]
> TIMEBASE=1/1000
> START=0
> ; 00:39:39
> END=2379000
> title=Start
>
> [CHAPTER]
> TIMEBASE=1/1000
> ; 00:39:39
> START=2379001
> ; 02:07:50
> END=7670000
> title=First Performance
>
> [CHAPTER]
> TIMEBASE=1/1000
> ; 02:07:50
> START=7670001
> ; 02:32:13
> END=9133000
> title=Break
>
> [CHAPTER]
> TIMEBASE=1/1000
> ; 02:32:13
> START=9133001
> ; 03:57:36
> END=14246000
> title=Second Performance
> ```

- write a new video file using the edited metadata file

```shell
ffmpeg -i INPUT.mp4 -i ffmetadata.txt -map_metadata 1 -codec copy OUTPUT.mp4
```
