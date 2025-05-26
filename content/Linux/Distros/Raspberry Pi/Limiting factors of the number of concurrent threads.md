---
{"publish":true,"cssclasses":""}
---


#threads #ulimit #stack #size

> [!info] Source
>
>

- check `ulimit -a`
- PID number too big
  - check `/proc/sys/kernel/threads-max`
  - check `/proc/sys/kernel/pid_max`
  - check `/sys/fs/cgroup/pids/user.slice/user-1000.slice/pids.max` and `/sys/fs/cgroup/pids/user.slice/user-1000.slice/pids.current` while blocking occurs
- most likely: stack size is too big
  - 8 MiB by default
  - each thread gets assigned memory of this size
  - however, there cannot be more threads than the amount of total physical memory divided by these 8 MiB
  - decreasing the stack size automatically increases the number of possible concurrent threads
  - **however: still check PID/threads settings above since these can now be a limiting factor**