---
{"publish":true,"created":"2025-05-15T09:01:48.763+02:00","modified":"2025-05-26T15:25:06.622+02:00","published":"2025-05-26T15:25:06.622+02:00","cssclasses":""}
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