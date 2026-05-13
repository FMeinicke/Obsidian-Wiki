---
publish: true
created: 2025-05-15T09:01:51.123+02:00
modified: 2025-05-26T15:25:12.153+02:00
published: 2025-05-26T15:25:12.153+02:00
cssclasses: ""
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
