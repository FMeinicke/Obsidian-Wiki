---
publish: true
created: 2024-12-06T06:58:20.117+01:00
modified: 2025-05-26T17:03:14.000+02:00
published: 2025-05-26T17:03:14.000+02:00
---

#zsh/array/length #zsh/array/empty

> [!info] Source(s)
>
> - <https://gist.github.com/fhuitelec/f900ba41fc6ed55199b2fff4dd226d4d>

```shell
(( ${#ARRAY[@]} == 0)) && {
    echo array empty
} || {
    echo array not empty
}
```
