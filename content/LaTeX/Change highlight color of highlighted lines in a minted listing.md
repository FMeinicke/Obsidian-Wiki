---
publish: true
created: 2025-05-15T09:01:48.732+02:00
modified: 2025-05-26T15:25:06.559+02:00
published: 2025-05-26T15:25:06.559+02:00
cssclasses: ""
---

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