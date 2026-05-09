---
publish: true
created: 2024-12-06T06:58:18.820+01:00
modified: 2025-05-26T17:03:05.000+02:00
published: 2025-05-26T17:03:05.000+02:00
---

#obsidian/css

> [!info] Source
>
> - <https://www.reddit.com/r/ObsidianMD/comments/s55zcw/comment/hswuttk>
> - <https://gist.github.com/vii33/f2c3a85b64023cefa9df6420730c7531>

add a [CSS snippet](https://help.obsidian.md/Extending+Obsidian/CSS+snippets) with the following content

```css
:root {
    --custom_line_width: 1100px;
}

body {
    --file-line-width: var(--custom_line_width) /* !important */;
}
```
