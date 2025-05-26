---
publish: true
sorting-spec: |-
  vim
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Paste in insert mode](Linux/Commands/vim/Paste in insert mode.md)
- [replace all occurrences](Linux/Commands/vim/replace all occurrences.md)
- [Replace with a newline](Linux/Commands/vim/Replace with a newline.md)

---



#vim/substitute

> [!info] Source
>
>

```vim
:%s/foo/bar/g
```



#vim/insert-mode #vim/paste

> [!info] Source(s)
> 
> - <https://stackoverflow.com/a/2861909/12780516>

- <kbd>Ctrl</kbd>+<kbd>R</kbd> followed by <kbd>*</kbd> will insert the contents of the clipboard
- <kbd>Ctrl</kbd>+<kbd>R</kbd> followed by <kbd>"</kbd> will insert the last delete or yank (the unnamed register)
- <kbd>Ctrl</kbd>+<kbd>R</kbd> followed by <kbd>{register}</kbd> will insert the contents of the specified register



#vim/substitute

> [!info] Source
> 
> - <https://stackoverflow.com/a/71334/12780516>

```vim
:%s/<search>/\r/g
```


---

## Tagged mentions


