---
{"publish":true,"cssclasses":""}
---

#latex/twoside #latex/if

> [!info] Source(s)
> 
> - <https://tex.stackexchange.com/a/360791/239888>

- this check is already provided by latex

```latex
\documentclass[
    twoside,
    ...
]{report}

% check for twoside
\if@twoside
    ...
\else
    ...
\fi

```