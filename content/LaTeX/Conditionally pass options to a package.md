---
{"publish":true,"created":"2025-05-15T09:01:48.794+02:00","modified":"2025-05-26T15:25:06.669+02:00","published":"2025-05-26T15:25:06.669+02:00","cssclasses":""}
---

#latex/if #latex/PassOptionsToPackage #latex/usepackage

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/124052/239888>

```latex
\if@somecondition
    \PassOptionsToPackage{<options>}{<package>}
\endif
%...
\usepackage[<more options>]{<package>}
```