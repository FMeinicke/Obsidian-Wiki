---
publish: true
created: 2026-06-05T11:17:17.455+02:00
modified: 2026-06-05T11:18:53.082+02:00
published: 2026-06-05T11:18:53.082+02:00
---

#find #ulimit #awk #printf #open-files

> [!info] Source
>
> - ChatGPT discussion

```bash
printf "%-8s %-30s %-15s %s\n" "PID" "Name" "soft/hard" "open files"
for pid in /proc/[0-9]*; do
    p=$(basename "$pid");
    name=$(ps -p "$p" -o comm= 2>/dev/null);
    limit=$(awk '/Max open files/ {print $4 "/" $5}' "$pid/limits" 2>/dev/null);
    [ -n "$limit" ] && printf "%-8s %-30s %-15s %s\n" "$p" "$name" "$limit" "$(ls "$pid/fd" 2>/dev/null | wc -l)";
done
```
