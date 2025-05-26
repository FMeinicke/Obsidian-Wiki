---
{"publish":true,"cssclasses":""}
---

#subfig #ref #subref

> [!info] Source(s)
> 
> - <https://tex.stackexchange.com/a/552633/239888>

```latex
\begin{figure}[H]
    \begin{subfigure}{0.49\textwidth}
        \includegraphics[]{img/Schema-Spritzenpumpe-aufliegend.drawio.png}
        \caption{\dots mit aufliegend gelagerter Spritze}%
        \label{subfig:Schema-Spritzenpumpe-aufliegend}
    \end{subfigure}
    \enspace
    \begin{subfigure}{0.49\textwidth}
        \includegraphics[]{img/Schema-Spritzenpumpe-endständig-alt.drawio.png}
        \caption{\dots mit endständig gelagerter Spritzenpumpen}%
        \label{subfig:Schema-Spritzenpumpe-endständig-alt}
    \end{subfigure}
    \caption{Schematischer Aufbau einer Spritzenpumpe}%
    \label{fig:schema_basic_syringe_pump}
\end{figure}%
\vspace{-5mm}%

We can link to a subfigure using \verb|\ref{subfig:Schema-Spritzenpumpe-endständig-alt}|. This produces the text \textit{1-1a}: \ref{subfig:Schema-Spritzenpumpe-endständig-alt}.

If we only want to have the \textit{a} (or \textit{b}) part of the number, we must use \verb|\subref{subfig:Schema-Spritzenpumpe-endständig-alt}|: \subref{subfig:Schema-Spritzenpumpe-endständig-alt}
```