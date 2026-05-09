---
publish: true
created: 2024-12-06T06:58:27.370+01:00
modified: 2025-05-26T17:04:19.000+02:00
published: 2025-05-26T17:04:19.000+02:00
---

#newif #if

> [!info] Source
>
> - <>

```latex
% Anlegen der Variable und setzen auf True
\newif\ifname\nametrue
% Ausführen von TeX-Code abhängig vom Wert der Variablen
\ifname
    Code falls _name=True_
\else
    Code falls _name=False_
\fi
```
