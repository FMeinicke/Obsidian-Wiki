---
publish: true
created: 2025-05-15T09:01:50.920+02:00
modified: 2025-05-26T15:25:11.513+02:00
published: 2025-05-26T15:25:11.513+02:00
cssclasses: ""
---

#systemd #journalctl #less

> [!info] Source
>
>

- set the `SYSTEM_LESS` environment variable
- by default this value is `FRSXMK`
- when overriding the variable be sure to include all of the desired default options as well
- to decrease the default horizontal scroll size, for example: `export SYSTEMD_LESS="FRSXMK -# 10"` (will scroll by 10 characters for each right/left arrow key press)