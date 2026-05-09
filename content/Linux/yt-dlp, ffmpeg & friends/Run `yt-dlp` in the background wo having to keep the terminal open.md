---
publish: true
created: 2024-12-06T06:58:08.878+01:00
modified: 2025-05-26T17:01:59.000+02:00
published: 2025-05-26T17:01:59.000+02:00
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
