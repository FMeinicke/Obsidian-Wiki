---
{"publish":true,"cssclasses":""}
---

#pwsh/ampersand #pwsh/dot #pwsh/sourcing #pwsh/scope

> [!info] Source
> 
> - <https://stackoverflow.com/a/54680512/12780516>

- **difference matters only** when calling PowerShell **scripts** or ***functions*** (or their ***aliases***) — for *cmdlets* and *external programs*, they act the *same*
- ***ampersand (`&`) — the call operator***
    - executes scripts and functions in a **child scope**
- ***dot (`.`) — the dot-sourcing operator***
    - executes scripts and functions in the **current (calling) scope**
    - typically used to modify the caller's scope, by adding functions, variables, etc. for later use