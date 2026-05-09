---
publish: true
created: 2024-12-06T06:58:08.908+01:00
modified: 2025-05-26T17:01:59.000+02:00
published: 2025-05-26T17:01:59.000+02:00
---

#latex/footnotemark #latex/footnotetext #latex/addtocounter

> [!info] Source
>
> - <https://tex.stackexchange.com/a/35045/239888>

```latex
Let's say we have a text\footnotemark{} which uses multiple \verb|\footnotemark{}|s in the same sentence.\footnotemark{}.
% If we now want to savely define the text for the first footnotemark, we first decrement the counter by one and then
% increment again afterwards.
\addtocounter{footnote}{-1}\addtocounter{Hfootnote}{-1}
\footnotetext{The first footnote.}
% Then we can define the text for the second footnotemark.
\addtocounter{footnote}{1}\addtocounter{Hfootnote}{1}
\footnotetext{The second footnote.}
```

This avoids hard-coding the footnote number for the `\footnotetext{}` commands which can lead to issues if the text before the two subsequent `\footnotemark{}`s adds more footnotes.
