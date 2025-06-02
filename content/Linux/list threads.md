---
{"publish":true,"cssclasses":""}
---


#threads

> [!info] Source
>
>

```shell
ps -eLf
```

  

- [Count number of threads + open files](Linux/Distros/Raspberry Pi/Count number of threads + open files.md)
- [Increase swap size](Linux/Distros/Raspberry Pi/Increase swap size.md)
- [Limiting factors of the number of concurrent threads](Linux/Distros/Raspberry Pi/Limiting factors of the number of concurrent threads.md)
- [RedHat XML VSCode extension](Linux/Distros/Raspberry Pi/RedHat XML VSCode extension.md)

---



#threads #open-files #ps #lsof #printf

> [!info] Source
>
>

```bash
search_proc="<PROC>"; while true; do t=$(ps -fLu pi | grep $search_proc$ | wc -l); t2=$(ps -eLf | wc -l); f=$(lsof | wc -l); printf '\b%.0s' {1..100}; printf "$search_proc$: $t, all: $t2; files: $f"; printf '%.0s' {1..100}; printf '\b%.0s' {1..100}; sleep 0.5; done
```



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



#swap #dphys-swapfile #swapon #swapoff

> [!info] Source
>
> - <https://diyusthad.com/2022/01/how-to-increase-swap-size-in-raspberry-pi.html>

```shell
sudo dphys-swapfile swapoff
sudo vim /etc/dphys-swapfile
#change CONF_SWAPSIZE= to a value in MB
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```



#vscode #vscode-extension #xml

> [!info] Source
>
>

- install `openjdk-11`
- configure the extension to use Java instead of the binary

---

## Tagged mentions

```dataviewjs
const pages = dv.pages('"Wiki"').where(page => !page.file.path.contains("Wiki/Linux/Distros/Raspberry Pi/"));

for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split("\n");

    let current_section_heading = "";

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        if (current_section_heading.length > 0 && line.startsWith("#")) {
            // https://regexr.com/85o2t
            // dv.paragraph(`${line}: ${/#[\w\/]*raspberry pi[\w\/]*/.test(line)}`);
            if (/#[\w\/]*raspberry pi[\w\/]*/.test(line)) {
                const page_file_path_basename = page.file.path.slice(0, -3);
                //dv.paragraph(`${page_file_path_basename}: ${current_section_heading}`);
                //dv.paragraph(`![[${page_file_path_basename}#${current_section_heading}]]`)
                dv.paragraph(`${page_file_path_basename.slice(5)}`);
                dv.paragraph(dv.sectionLink(page_file_path_basename, current_section_heading, true));
            }
            current_section_heading = "";
        }

        if (line.startsWith("## ")) {
            current_section_heading = line.slice(3);
        }
    }
}
```
