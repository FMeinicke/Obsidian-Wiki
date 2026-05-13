---
publish: true
created: 2025-05-15T09:01:49.232+02:00
modified: 2025-05-26T15:25:07.731+02:00
published: 2025-05-26T15:25:07.731+02:00
cssclasses: ""
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