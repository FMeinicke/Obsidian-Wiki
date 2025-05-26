---
{"publish":true,"cssclasses":""}
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