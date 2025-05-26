---
{"publish":true,"cssclasses":""}
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
