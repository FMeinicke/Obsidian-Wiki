---
{"publish":true,"cssclasses":""}
---

#systemd #journalctl #less

> [!info] Source
>
>

- set the `SYSTEM_LESS` environment variable
- by default this value is `FRSXMK`
- when overriding the variable be sure to include all of the desired default options as well
- to decrease the default horizontal scroll size, for example: `export SYSTEMD_LESS="FRSXMK -# 10"` (will scroll by 10 characters for each right/left arrow key press)