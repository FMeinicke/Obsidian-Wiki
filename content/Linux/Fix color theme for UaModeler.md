---
{"publish":true,"created":"2025-05-15T09:01:50.217+02:00","modified":"2025-05-26T15:25:10.169+02:00","published":"2025-05-26T15:25:10.169+02:00","cssclasses":""}
---


#kde/plasma #kde/plasma/color-themes #trolltech-conf #uamodeler

> [!info] Source(s)
> 
> - manual working out that UaModeler is a Qt4 app (inspecting the AppImage <https://docs.appimage.org/user-guide/run-appimages.html#mount-an-appimage>)
> - `~/.config/Trolltech.conf`: <https://wiki.archlinux.org/title/Qt#Styles_in_Qt_4>

- UaModeler look bad in dark mode since some things are still using light colors
- the only way to use a light color theme is to change the global plasma theme
- turns out, UaModeler is a Qt4 application which actually only seems to rely on `~/.config/Trolltech.conf`
- Qt5/6 applications respect the `*.color` files in `~/.config/color-schemes/` or `/usr/share/color-schemes/` (at least they don't seem to be affected by changes in `~/.config/Trolltech.conf`)
- so, to just change UaModeler to a light theme but have the rest use a dark theme, we can simply change `~/.config/Trolltech.conf` to use the configuration for the light theme
    - switch Plasma to Breath Light
    - save `~/.config/Trolltech.conf` to e.g. `~/.config/Trolltech-breath-light.conf`
    - switch back to Breath Dark
    - copy `~/.config/Trolltech-breath-light.conf` to `~/.config/Trolltech.conf`
    - UaModeler is now in light mode

> [!WARNING] ATTENTION
> Due to the nature of this workaround, every time the Plasma theme is changed, `~/.config/Trolltech.conf` is changed, as well. Therefore, it has to be changed to the light theme manually every time to ensure UaModeler is using the light theme.

> [!info] Note
> Funnily enough, UaExpert on the other hand is a Qt5 app, which adheres much better to the global color theme.