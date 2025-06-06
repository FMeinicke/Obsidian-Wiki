---
{"publish":true,"cssclasses":""}
---

#spacing

> [!info] Source
>
> - verbatim from <https://tex.stackexchange.com/a/74354/239888>

There are a number of horizontal spacing macros for LaTeX:

1. `\,` inserts a `.16667em` space in text mode, or `\thinmuskip` (equivalent to `3mu`) in math mode; there's an equivalent `\thinspace` macro;
2. `\!` is the *negative* equivalent to `\,`; there's an equivalent `\negthinspace` macro;
3. `\>` (or `\:`) inserts a `.2222em` space in text mode, or `\medmuskip` (equivalent to `4.0mu plus 2.0mu minus 4.0mu`) in math mode; there's an equivalent `\medspace`;
4. `\negmedspace` is the *negative* equivalent to `\medspace`;
5. `\;` inserts a `.2777em` space in text mode, or `\thickmuskip` (equivalent to `5.0mu plus 5.0mu`) in math mode; there's an equivalent `\thickspace`;
6. `\negthickspace` is the *negative* equivalent to `\thickspace`;
7. `\enspace` inserts a space of `.5em` in text or math mode;
8. `\quad` inserts a space of `1em` in text or math mode;
9. `\qquad` inserts a space of `2em` in text or math mode;
10. `\kern <len>` inserts a skip of `<len>` (may be negative) in text or math mode (a plain TeX skip); there's also a `m`ath-specific `\mkern <math len>`;
11. `\hskip <len>` (similar to `\kern`);
12. `\hspace{<len>}` inserts a space of length `<len>` (may be negative) in math or text mode (a LaTeX `\hskip`);
13. `\hphantom{<stuff>}` inserts space of length equivalent to `<stuff>` in math or text mode. `\phantom{<stuff>}` is similar, inserting a horizontal and vertical space that matches `<stuff>`. Should be `\protect`ed when used in fragile commands (like `\caption` and sectional headings);
14. <code>\ </code>&nbsp;inserts what is called a "control space" (in text or math mode);
15. <code> </code> inserts an inter-word space in text mode (and is gobbled in math mode). Similarly for `\space` and `{ }`.
16. `~`&nbsp;inserts an "unbreakable" space (similar to an HTML `&nbsp;`) (in text or math mode);
17. `\hfill` inserts a so-called "rubber length" or stretch between elements (in text or math mode). Note that you may need to provide a type of anchor to fill from/to; see [What is the difference between `\hspace*{\fill}` and `\hfill`?](https://tex.stackexchange.com/q/45948/5764);

Your usage *should* work in *math mode*, so try `$\:$`.

[![enter image description here][1]][1]

```latex
    \documentclass{article}

    \usepackage[margin=1in]{geometry}% Just for this example
    \setlength{\parindent}{0pt}% Just for this example

    \begin{document}

    There are a number of horizontal spacing macros for LaTeX:

    \begin{tabular}{lp{5cm}}
      \verb|a\,b|                     & a\,b \quad $a\, b$ \\
      \verb|a\thinspace b|            & a\thinspace b \quad $a\thinspace b$ \\
      \verb|a\!b|                     & a\!b \quad $a\!b$ \\
      \verb|a\negthinspace b|         & a\negthinspace b \quad $a\negthinspace b$ \\
      \verb|a\:b|                     & a\:b \quad $a\:b$ \\
      \verb|a\>b|                     & a\>b \quad $a\>b$ \\
      \verb|a\medspace b|             & a\medspace b \quad $a\medspace b$ \\
      \verb|a\negmedspace b|          & a\negmedspace b \quad $a\negmedspace b$ \\
      \verb|a\;b|                     & a\;b \quad $a\;b$ \\
      \verb|a\thickspace b|           & a\thickspace b \quad $a\thickspace b$ \\
      \verb|a\negthickspace b|        & a\negthickspace b \quad $a\negthickspace b$ \\
      \verb|$a\mkern\thinmuskip b$|   & $a\mkern\thinmuskip b$ (similar to \verb|\,|) \\
      \verb|$a\mkern-\thinmuskip b$|  & $a\mkern-\thinmuskip b$ (similar to \verb|\!|) \\
      \verb|$a\mkern\medmuskip b$|    & $a\mkern\medmuskip b$ (similar to \verb|\:| or \verb|\>|) \\
      \verb|$a\mkern-\medmuskip b$|   & $a\mkern-\medmuskip b$ (similar to \verb|\negmedspace|) \\
      \verb|$a\mkern\thickmuskip b$|  & $a\mkern\thickmuskip b$ (similar to \verb|\;|) \\
      \verb|$a\mkern-\thickmuskip b$| & $a\mkern-\thickmuskip b$ (similar to \verb|\negthickspace|) \\
      \verb|a\enspace b|              & a\enspace b \\
      \verb|$a\enspace b$|            & $a\enspace b$ \\
      \verb|a\quad b|                 & a\quad b \\
      \verb|$a\quad b$|               & $a\quad b$ \\
      \verb|a\qquad b|                & a\qquad b \\
      \verb|$a\qquad b$|              & $a\qquad b$ \\
      \verb|a\hskip 1em b|            & a\hskip 1em b \\
      \verb|$a\hskip 1em b$|          & $a\hskip 1em b$ \\
      \verb|a\kern 1pc b|             & a\kern 1pc b \\
      \verb|$a\kern 1pc b$|           & $a\kern 1pc b$ \\
      \verb|$a\mkern 17mu b$|         & $a\mkern 17mu b$ \\
      \verb|a\hspace{35pt}b|          & a\hspace{35pt}b \\
      \verb|$a\hspace{35pt}b$|        & $a\hspace{35pt}b$ \\
      \verb|axyzb|                    & axyzb \\
      \verb|a\hphantom{xyz}b|         & a\hphantom{xyz}b (or just \verb|\phantom|) \\
      \verb|$axyzb$|                  & $axyzb$ \\
      \verb|$a\hphantom{xyz}b$|       & $a\hphantom{xyz}b$ (or just \verb|\phantom|) \\
      \verb|a b|                      & a b \\
      \verb|$a b$|                    & $a b$ \\
      \verb|a\space b|                & a\space b \\
      \verb|$a\space b$|              & $a\space b$ \\
      \verb|a\ b|                     & a\ b \\
      \verb|$a\ b$|                   & $a\ b$ \\
      \verb|a{ }b|                    & a{ }b \\
      \verb|$a{ }b$|                  & $a{ }b$ \\
      \verb|a~b|                      & a~b \\
      \verb|$a~b$|                    & $a~b$ \\
      \verb|a\hfill b|                & a\hfill b \\
      \verb|$a\hfill b$|              & $a\hfill b$$
    \end{tabular}

    \end{document}
```

  [1]: https://i.stack.imgur.com/xaQvv.png