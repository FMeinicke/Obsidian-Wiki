---
{"publish":true,"cssclasses":""}
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