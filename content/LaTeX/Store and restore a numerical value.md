---
{"publish":true,"created":"2025-05-15T09:01:49.123+02:00","modified":"2025-05-26T15:25:07.450+02:00","published":"2025-05-26T15:25:07.450+02:00","cssclasses":""}
---

#latex/edef #latex/setlength #latex/fboxrule

> [!info] Source(s)
> 
> - <https://tex.stackexchange.com/a/366237/239888>
> - <https://tex.stackexchange.com/a/145073/239888>

```latex
% store the value
\edef\savedfboxrule{\the\fboxrule}
% set it to something else (e.g. if the following images should not have a border)
\setlength{\fboxrule}{0pt}

...

% restore the saved value
\setlength{\fboxrule}{\savedfboxrule}
```

- the `\setlength` command also seems to be scoped to environments, i.e., if used inside a `\begin{table}...\end{table}`, then the change only applies up to the `\end`