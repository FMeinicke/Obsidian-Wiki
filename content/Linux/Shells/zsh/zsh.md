---
publish: true
sorting-spec: |-
  zsh
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Check if array is empty](Linux/Shells/zsh/Check if array is empty.md)

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

---

## Tagged mentions


