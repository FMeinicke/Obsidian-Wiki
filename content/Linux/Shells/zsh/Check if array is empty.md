---
publish: true
created: 2025-05-15T09:01:50.686+02:00
modified: 2025-05-26T15:25:11.419+02:00
published: 2025-05-26T15:25:11.419+02:00
cssclasses: ""
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