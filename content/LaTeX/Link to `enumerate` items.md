---
publish: true
created: 2024-12-06T06:58:22.697+01:00
modified: 2025-05-26T17:03:38.000+02:00
published: 2025-05-26T17:03:38.000+02:00
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
