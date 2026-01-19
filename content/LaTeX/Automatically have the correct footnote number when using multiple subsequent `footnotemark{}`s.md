---
publish: true
created: 2025-05-15T09:01:48.685+02:00
modified: 2025-05-26T15:25:06.434+02:00
published: 2025-05-26T15:25:06.434+02:00
cssclasses: ""
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