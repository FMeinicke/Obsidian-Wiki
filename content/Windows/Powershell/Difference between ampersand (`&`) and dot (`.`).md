---
publish: true
created: 2024-12-06T06:58:11.091+01:00
modified: 2025-05-27T08:42:41.000+02:00
published: 2025-05-27T08:42:41.000+02:00
---

#pwsh/ampersand #pwsh/dot #pwsh/sourcing #pwsh/scope

> [!info] Source
>
> - <https://stackoverflow.com/a/54680512/12780516>

- **difference matters only** when calling PowerShell **scripts** or _**functions**_ (or their _**aliases**_) — for _cmdlets_ and _external programs_, they act the _same_
- _**ampersand (`&`) — the call operator**_
  - executes scripts and functions in a **child scope**
- _**dot (`.`) — the dot-sourcing operator**_
  - executes scripts and functions in the **current (calling) scope**
  - typically used to modify the caller's scope, by adding functions, variables, etc. for later use
