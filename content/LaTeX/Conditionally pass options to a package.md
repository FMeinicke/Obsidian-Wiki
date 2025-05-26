---
{"publish":true,"cssclasses":""}
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