---
publish: true
sorting-spec: |-
  Shells
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Redirection syntax](Linux/Shells/Redirection syntax.md)
    
- [bash](bash)
    
    - [Command Line](Command Line)
        
    - [General](General)
        
        - [Divide variables](Linux/Shells/bash/General/Divide variables.md)
        - [Escape single quotes inside single quotes](Linux/Shells/bash/General/Escape single quotes inside single quotes.md)
        - [Get a random integer value](Linux/Shells/bash/General/Get a random integer value.md)
        - [Move cursor to start of line to print over the line](Linux/Shells/bash/General/Move cursor to start of line to print over the line.md)
        - [no-op](Linux/Shells/bash/General/no-op.md)
        - [Print variable name and value](Linux/Shells/bash/General/Print variable name and value.md)
    - [Scripting](Scripting)
        
        - [Run command stored in a string](Linux/Shells/bash/Scripting/Run command stored in a string.md)
- [zsh](zsh)
    
    - [Check if array is empty](Linux/Shells/zsh/Check if array is empty.md)

---



#shell/redirect #shell/pipe #shell/stdout #shell/stderr #shell/file-descriptor

> [!info] Source
> 
> - <https://rednafi.com/misc/shell_redirection/>

- **Redirect stdout**: `command > file`
- **Redirect stderr**: `command 2> file`
- **Redirect both stdout and stderr**:
    - Standard: `command > file 2>&1`
    - Shorthand: `command &> file`
- **Append stdout**: `command >> file`
- **Append both stdout and stderr**:
    - Standard: `command >> file 2>&1`
    - Shorthand: `command &>> file`
- **Pipe stdout**: `command1 | command2`
- **Pipe both stdout and stderr**:
    - Standard: `command1 2>&1 | command2`
    - Shorthand: `command1 |& command2`
- **Custom file descriptors**:
    - Create and redirect stdout: `exec 3> file; command >&3`
    - Redirect stderr: `command 2>&3`
    - Redirect both stdout and stderr: `command > /dev/fd/3 2>&1` (no shorthand available)
- **Discard stdout and stderr**:
    - Standard: `command > /dev/null 2>&1`
    - Shorthand: `command &>/dev/null`

---

---

## Tagged mentions


