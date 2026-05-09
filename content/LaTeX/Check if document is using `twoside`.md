---
publish: true
created: 2024-12-06T06:58:18.577+01:00
modified: 2025-05-26T17:03:05.000+02:00
published: 2025-05-26T17:03:05.000+02:00
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
