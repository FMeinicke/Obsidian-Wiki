---
publish: true
sorting-spec: |-
  LaTeX
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [`newif`](LaTeX/`newif`.md)
- [Automatically have the correct footnote number when using multiple subsequent `footnotemark{}`s](LaTeX/Automatically have the correct footnote number when using multiple subsequent `footnotemark{}`s.md)
- [Bullets without an `itemize` environment](LaTeX/Bullets without an `itemize` environment.md)
- [Change highlight color of highlighted lines in a minted listing](LaTeX/Change highlight color of highlighted lines in a minted listing.md)
- [Check if document is using `twoside`](LaTeX/Check if document is using `twoside`.md)
- [Conditionally pass options to a package](LaTeX/Conditionally pass options to a package.md)
- [Dimensions](LaTeX/Dimensions.md)
- [Fix `(Fatal format file error; I'm stymied)`](LaTeX/Fix `\(Fatal format file error; I'm stymied\)`.md)
- [Horizontal spacing](LaTeX/Horizontal spacing.md)
- [Link to `enumerate` items](LaTeX/Link to `enumerate` items.md)
- [Make `itemize` `item`s linkable](LaTeX/Make `itemize` `item`s linkable.md)
- [Make a color less bright a.k.a. pseudo-transparent](LaTeX/Make a color less bright a.k.a. pseudo-transparent.md)
- [Only link to subfig number](LaTeX/Only link to subfig number.md)
- [Prevent hyphenation of a single word](LaTeX/Prevent hyphenation of a single word.md)
- [Print lengths in human-readable units](LaTeX/Print lengths in human-readable units.md)
- [Reduce space after captions of floating environments (like figures, tables, listings, ...)](LaTeX/Reduce space after captions of floating environments \(like figures, tables, listings, ...\).md)
- [Reference the same footnote multiple times](LaTeX/Reference the same footnote multiple times.md)
- [Rotate images in figures](LaTeX/Rotate images in figures.md)
- [Store and restore a numerical value](LaTeX/Store and restore a numerical value.md)
- [Typeset corresponds to a.k.a. equals with a hat](LaTeX/Typeset corresponds to a.k.a. equals with a hat.md)
- [Underlines in drawio SVG diagrams](LaTeX/Underlines in drawio SVG diagrams.md)
- [Untitled](LaTeX/Untitled.md)
- [Usage of different dashes](LaTeX/Usage of different dashes.md)

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

Your usage *should* work in *math mode*, so try `$\:---
publish: true
sorting-spec: |-
  LaTeX
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [`newif`](LaTeX/`newif`.md)
- [Automatically have the correct footnote number when using multiple subsequent `footnotemark{}`s](LaTeX/Automatically have the correct footnote number when using multiple subsequent `footnotemark{}`s.md)
- [Bullets without an `itemize` environment](LaTeX/Bullets without an `itemize` environment.md)
- [Change highlight color of highlighted lines in a minted listing](LaTeX/Change highlight color of highlighted lines in a minted listing.md)
- [Check if document is using `twoside`](LaTeX/Check if document is using `twoside`.md)
- [Conditionally pass options to a package](LaTeX/Conditionally pass options to a package.md)
- [Dimensions](LaTeX/Dimensions.md)
- [Fix `(Fatal format file error; I'm stymied)`](LaTeX/Fix `\(Fatal format file error; I'm stymied\)`.md)
- [Horizontal spacing](LaTeX/Horizontal spacing.md)
- [Link to `enumerate` items](LaTeX/Link to `enumerate` items.md)
- [Make `itemize` `item`s linkable](LaTeX/Make `itemize` `item`s linkable.md)
- [Make a color less bright a.k.a. pseudo-transparent](LaTeX/Make a color less bright a.k.a. pseudo-transparent.md)
- [Only link to subfig number](LaTeX/Only link to subfig number.md)
- [Prevent hyphenation of a single word](LaTeX/Prevent hyphenation of a single word.md)
- [Print lengths in human-readable units](LaTeX/Print lengths in human-readable units.md)
- [Reduce space after captions of floating environments (like figures, tables, listings, ...)](LaTeX/Reduce space after captions of floating environments \(like figures, tables, listings, ...\).md)
- [Reference the same footnote multiple times](LaTeX/Reference the same footnote multiple times.md)
- [Rotate images in figures](LaTeX/Rotate images in figures.md)
- [Store and restore a numerical value](LaTeX/Store and restore a numerical value.md)
- [Typeset corresponds to a.k.a. equals with a hat](LaTeX/Typeset corresponds to a.k.a. equals with a hat.md)
- [Underlines in drawio SVG diagrams](LaTeX/Underlines in drawio SVG diagrams.md)
- [Untitled](LaTeX/Untitled.md)
- [Usage of different dashes](LaTeX/Usage of different dashes.md)

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

.

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
      \verb|$a\hfill b$|              & $a\hfill b$
    \end{tabular}

    \end{document}
```

  [1]: https://i.stack.imgur.com/xaQvv.png


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


#latex/stymied

> [!info] Source(s)
> 
> - <https://texfaq.org/FAQ-formatstymy>

- to regenerate the format on a Unix system run

```shell
sudo fmtutil -sys --all
```

- or install the `texlive-xetex` package (on Arch-based distros; name may differ for other distros)


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


#latex/twoside #latex/if

> [!info] Source(s)
> 
> - <https://tex.stackexchange.com/a/360791/239888>

- this check is already provided by latex

```latex
\documentclass[
    twoside,
    ...
]{report}

% check for twoside
\if@twoside
    ...
\else
    ...
\fi

```


#latex/dimension #latex/pt #latex/pc #latex/mm #latex/mm

> [!info] Source(s)
> 
> - <https://wiki.contextgarden.net/Dimensions>

| unit         | TeX name | in sp     | in pt   | in pc  | in dd   | in cc  | in bp   | in in   | in mm  | in cm   |
|--------------|----------|-----------|---------|--------|---------|--------|---------|---------|--------|---------|
| scaled point | sp       | 1         | 1/65536 |        |         |        |         |         |        |         |
| point        | pt       | 65536     | 1       | 1/12   | 0.9346  | 0.0779 | 0.9963  | 1/72.27 | 0.3516 | 0.0351  |
| pica         | pc       | 786432    | 12      | 1      | 11.2149 | 0.9346 | 11.9552 | 0.1660  | 4.2175 | 0.4218  |
| didot        | dd       | 70124.081 | 1.0700  | 0.0892 | 1       | 1/12   | 1.0660  | 0.0148  | 0.3761 | 0.0376  |
| cicero       | cc       | 841488.98 | 12.8401 | 1.0700 | 12      | 1      | 12.7921 | 0.1777  | 4.5128 | 0.45128 |
| big point    | bp       | 65781.76  | 1.0038  | 0.0836 | 0.9381  | 0.0782 | 1       | 1/72    | 0.3528 | 0.0353  |
| inch         | in       | 4736286.7 | 72.27   | 6.0225 | 67.5415 | 5.6284 | 72      | 1       | 25.4   | 2.54    |
| millimeter   | mm       | 186467.98 | 2.8453  | 0.2371 | 2.6591  | 0.2216 | 2.8346  | 0.0394  | 1      | 0.1     |
| centimeter   | cm       | 1864679.8 | 28.4528 | 2.3711 | 26.5911 | 2.2159 | 28.3464 | 0.39370 | 10     | 1       |


#latex/itemize/item #latex/label #latex/hyperref #latex/clevref #latex/crefname #latex/cref #latex/ref #latex/xpatch #latex/refcount #latex/newcounter #latex/setcounter #latex/AtBeginEnvironment #latex/addtoextras

> [!info] Source(s)
> 
> - <https://tex.stackexchange.com/a/296099/239888>
> - <https://tex.stackexchange.com/a/180192/239888>

```latex

% make itemize environments have a counter so we can link to individual items using `\label's
% source: https://tex.stackexchange.com/a/296099/239888
\usepackage{xpatch}
\usepackage{refcount}

\newcounter{itemcntr}

\AtBeginEnvironment{itemize}{%
    \setcounter{itemcntr}{0}%
    \xapptocmd{\item}{\refstepcounter{itemcntr}}{}{}
}


\usepackage[ngerman]{cleveref}

% source: https://tex.stackexchange.com/a/180192/239888
\crefname{itemcntr}{item}{items}
\addto\extrasngerman{\crefname{itemcntr}{Punkt}{Punkte}}

\newcommand{\itemref}[1]{\hyperref[{#1}]{\cref*{#1}\ \ref*{#1}}}
```


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


#latex/hyphenation #latex/mbox

> [!info] Source
> 
> - <https://texfaq.org/FAQ-wdnohyph>

```latex
This \mbox{word} will not be hyphenated.
```


#latex/hyphen #latex/textendash #latex/textemdash

> [!info] Source
> 
> - <https://zhanksun.github.io/posts/en-dashes-em-dashes/>

- there are three main types (lengths) of dashes
    - the hyphen `-`,
        - it's used for inter-word hyphenation like *"well-being"*
    - the en-dash `\textendash{}` which is slightly longer than the hyphen, and
        - it's used for ranges, e.g., `July 9 \textendash{} August 17` or `pp. 37 \textendash{} 59`
    - the em-dash `\textemdash{}` which is even longer than the en-dash
        - it's used for strong breaks, where a comma might be too subtle, e.g., `We bought markers, paper, pens, and tablets \textemdash{} all of which were on sale, of course \textemdash{} for our clients to use in the courtroom.`, or
        - to separate words from each other in a title, e.g., `\section{Der kontinuierliche Fluss \textemdash{} Contiflow}`


#latex/caption #latex/spacing #latex/floats #latex/figure #latex/table #latex/listing #latex/setlength #latex/belowcaptionskip #latex/textfloatsep

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/23315/239888>
> - <https://tex.stackexchange.com/a/23316/239888>

```latex
% in the preamble

% default: 0pt
\setlength{\belowcaptionskip}{-10pt}
% default: 20.0pt plus 2.0pt minus 4.0pt
\setlength{\textfloatsep}{10.0pt plus 2.0pt minus 4.0pt}
```

- note that the `\belowcaptionskip` also affects the space between subcaptions and the main caption, so setting this too small could squash these too close together and might look ugly


#latex/if #latex/PassOptionsToPackage #latex/usepackage

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/124052/239888>

```latex
\if@somecondition
    \PassOptionsToPackage{<options>}{<package>}
\endif
%...
\usepackage[<more options>]{<package>}
```


#latex/textbullet #latex/font-size

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/152528/239888>
> - <https://comp.text.tex.narkive.com/RRElJoAu/a-bullet-smaller-than-textbullet-but-larger-than-cdot#post5>

```latex
This \textbullet\ is a bullet \textbullet\ in the text.
```

To change the bullet's size, simply wrap it in braces and change the font size:

```latex
This {\Large\textbullet}\ is a larger bullet, and this {\footnotesize\textbullet}\ is a very small bullet.
```


#latex/footref #latex/footnote #latex/label

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/368659/239888> (this actually suggests creating the command `\footref` but it appears that it's already included in latex-dev)

- add a `\label` to the `\footnote` to reference, then use `\footref` to reference it:

```latex
Let's say we awant to reference a certain footnote here.\footref{fn:example}
Like this one.\footnote{\label{fn:example}This is the footnote.}
And then later again.\footref{fn:example}
```


#latex/figure #latex/includegraphics/angle #latex/textwidth

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/50073/239888>

```latex
\begin{figure}[ht]
    \includesvg[angle=90,width=0.9\textheight]{Modelling-SyringePumpComponentType.drawio.svg}
    \caption{Grafische Darstellung des \english{SyringePumpComponentType} im Informationsmodell}%
    \label{fig:Modelling-SyringePumpComponentType}
\end{figure}%
```


#latex/lengths #latex/layouts #latex/prntlen #latex/textwidth

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/39385/239888>

```latex
\usepackage{layouts}

\begin{document}
    \printinunitsof{cm}\prntlen{\textwidth}
\end{document}
```


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


#latex/xcolor #latex/color

> [!info] Source
> 
> - <https://ctan.mirror.norbert-ruehl.de/macros/latex/contrib/xcolor/xcolor.pdf>

```latex
\usepackage[svgnames]{xcolor}

\begin{document}
    Normal cyan: \color{Cyan}\\
    Very light cyan: \color{Cyan!20}
\end{dpcument}
```


#latex/minted #latex/xglobal #latex/colorlet #latex/FancyVerbHighlightColor #latex/xcolor

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/682602/239888>

- use `\xglobal\colorlet{FancyVerbHighlightColor}{<color>}` inside the listing (escaping must be enabled!)

```latex
\begin{listing}[htb]
    \begin{minted}[autogobble,escapeinside=||,highlightlines={3,14,7,18}]{python}
        # syringe_pump.py
        class SyringePump(BaseSyringePump):
            def __init__(self, server, syringe_pump_backend) -> None:
                super().__init__(server, syringe_pump_backend)
                # ...
            |\xglobal\colorlet{FancyVerbHighlightColor}{Fuchsia!8}|
            async def init(self) -> None:
                # ...
            |\xglobal\colorlet{FancyVerbHighlightColor}{Cyan!11}| % this seems to be the default color or at least close enough
        # cetoni_syringe_pump.py
        class CetoniSyringePumpDevice(Device):
            def __init__(self, server, syringe_pump_backend) -> None:
                super().__init__(server, syringe_pump_backend)
                self.syringe_pump = SyringePump(server, syringe_pump_backend)
                # ...
            |\xglobal\colorlet{FancyVerbHighlightColor}{Fuchsia!8}|
            async def init(self) -> None:
                await self.syringe_pump.init()
                # ...
    \end{minted}
    \unskip
    \caption{}%
    \label{lst:implementation_basics_async_init}
\end{listing}
```

---
publish: true
title: Typeset "corresponds to" a.k.a. "equals with a hat"
cssclasses:
  - hide_properties
---

#latex/mathrel #latex/hat #obsidian

> [!info] Source
> 
> - <https://tex.stackexchange.com/questions/103408/symbol-for-corresponds-to-equals-sign-with-hat>

```latex
\hat{=}
% or
\mathrel{\hat{=}} % better in Obsidian
```

---

## Tagged mentions


