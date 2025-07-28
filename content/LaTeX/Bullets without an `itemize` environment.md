---
{"publish":true,"created":"2025-05-15T09:01:48.716+02:00","modified":"2025-05-26T15:25:06.497+02:00","published":"2025-05-26T15:25:06.497+02:00","cssclasses":""}
---

#latex/textbullet #latex/font-size

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/152528/239888>
> - <https://comp.text.tex.narkive.com/RRElJoAu/a-bullet-smaller-than-textbullet-but-larger-than-cdot#post5>

```latex
This \textbullet\ is a bullet \textbullet\ in the text.
```

To change the bullet's size, simply wrap it in braces and change the font size:

```latex
This {\Large\textbullet}\ is a larger bullet, and this {\footnotesize\textbullet}\ is a very small bullet.
```