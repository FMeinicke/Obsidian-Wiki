---
{"publish":true,"created":"2025-05-15T09:01:49.076+02:00","modified":"2025-05-26T15:25:07.372+02:00","published":"2025-05-26T15:25:07.372+02:00","cssclasses":""}
---

#latex/footref #latex/footnote #latex/label

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/368659/239888> (this actually suggests creating the command `\footref` but it appears that it's already included in latex-dev)

- add a `\label` to the `\footnote` to reference, then use `\footref` to reference it:

```latex
Let's say we awant to reference a certain footnote here.\footref{fn:example}
Like this one.\footnote{\label{fn:example}This is the footnote.}
And then later again.\footref{fn:example}
```