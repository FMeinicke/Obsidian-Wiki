---
publish: true
created: 2025-05-15T09:01:48.951+02:00
modified: 2025-05-26T15:25:07.091+02:00
published: 2025-05-26T15:25:07.091+02:00
cssclasses: ""
---

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