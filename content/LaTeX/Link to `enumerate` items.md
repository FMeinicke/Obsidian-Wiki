---
{"publish":true,"created":"2025-05-15T09:01:48.935+02:00","modified":"2025-05-26T15:25:07.012+02:00","published":"2025-05-26T15:25:07.012+02:00","cssclasses":""}
---

#latex/enumerate #latex/label #latex/ref

> [!info] Source(s)
> 
> - <>

```latex
\begin{enumerate}
    \item foo\label{itm:foo}
    \item bar\label{itm:bar}
         lorem ipsum
    \item baz\label{itm:baz}
\end{enumerate}

This option \ref{itm:foo} comes before \ref{itm:baz}.
```