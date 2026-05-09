---
publish: true
created: 2024-12-06T06:58:17.200+01:00
modified: 2025-05-26T17:02:58.000+02:00
published: 2025-05-26T17:02:58.000+02:00
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
