---
publish: true
sorting-spec: |-
  yt-dlp, ffmpeg & friends
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Add chapters to a video file using `ffmpeg`](Linux/yt-dlp, ffmpeg & friends/Add chapters to a video file using `ffmpeg`.md)
- [Convert `.webm` to `.mp4`](Linux/yt-dlp, ffmpeg & friends/Convert `.webm` to `.mp4`.md)
- [Run `yt-dlp` in the background wo having to keep the terminal open](Linux/yt-dlp, ffmpeg & friends/Run `yt-dlp` in the background wo having to keep the terminal open.md)
- [Use `ffmpeg` to manually merge audio and video files from `yt-dlp`](Linux/yt-dlp, ffmpeg & friends/Use `ffmpeg` to manually merge audio and video files from `yt-dlp`.md)

---



#yt-dlp #nohup #bg #disown

> [!info] Source
> 
> - <https://smcleod.net/2018/07/run-youtube-dl-or-similar-in-the-background/>

- prefix the command with `nohup`

```shell
nohup yt-dlp [OPTIONS] URL & disown
# now you can logout of the terminal and the download will still continue
```

- progress can be viewed by `tail`ing `nohup.out`

```shell
tail -f nohup.out
```




#ffmpeg #yt-dlp 

> [!info] Source(s)
> 
> - <https://www.reddit.com/r/ffmpeg/comments/100nhxj/comment/j2mavec/>

```shell
ffmpeg -i video_file.mp4 -i audio_file.m4a -c:v copy -c:a copy out_file.mp4
```



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



#ffmpeg 

> [!info] Source
> 
> - <https://stackoverflow.com/a/60443156/12780516>

```shell
ffmpeg -i input.webm -c copy output.mp4
```

---

## Tagged mentions


