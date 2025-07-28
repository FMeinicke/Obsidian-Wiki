---
{"publish":true,"created":"2025-05-15T09:01:49.169+02:00","modified":"2025-05-26T15:25:07.559+02:00","published":"2025-05-26T15:25:07.559+02:00","cssclasses":""}
---

#latex/includesvg/inkscapeformat

> [!info] Source
> 
> - trial and error
> - <https://gitlab.com/inkscape/inkscape/-/issues/952/>
> - <https://ctan.mirror.norbert-ruehl.de/graphics/svg/doc/svg.pdf>

- the default PDF exporter from Inkscape can't correctly export underlined text; this is a long standing [issue](https://gitlab.com/inkscape/inkscape/-/issues/952/) that hasn't been resolved yet
- the only solution to display the underlined text correctly, is to use the PNG exporter, instead

```latex
\begin{figure}[htb]
    \includesvg[width=0.99\textwidth,inkscapeformat=png]{Server-Implementation-Components-Schema.drawio.svg}
    \caption{Schematische Darstellung der Softwarekomponenten und ihren Beziehungen}%
    \label{fig:Server-Implementation-Components-Schema}
\end{figure}%
```