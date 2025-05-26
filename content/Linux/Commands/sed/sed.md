---
publish: true
sorting-spec: |-
  sed
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Comment and uncomment lines](Linux/Commands/sed/Comment and uncomment lines.md)
- [Multiple commands](Linux/Commands/sed/Multiple commands.md)
- [Using different delimiters](Linux/Commands/sed/Using different delimiters.md)

---



#sed

> [!info] Source
>
> - <https://stackoverflow.com/a/27355109/12780516>

- to comment a line (and preserve indentation)

  ```shell
  sed -Ei '/<pattern>/s/^(\s*)/\1# /g'
  ```

- to uncomment a line (and preserve indentation)

  ```shell
  sed -Ei '/<pattern>/s/^(\s*)#\s?/\1/g'
  ```



#sed

> [!info] Source
>
>

- simply concatenate the commands with `;`

  ```shell
  sed -n 's/\.//g;s/!define VERSION //p' "${0%/*}/setup.nsi"
  ```

- alternatively you could use multiple `-e`'s

  ```shell
  sed -n -e 's/\.//g' -e 's/!define VERSION //p' "${0%/*}/setup.nsi"
  ```

- the `-n` option causes `sed` to only output changed lines (in combination with the `p` command at the end)



#sed

> [!info] Source
>
> - <https://backreference.org/2010/02/20/using-different-delimiters-in-sed/index.html>

```shell
#do this (ugly)...
sed '/\/a\/b\/c\//{do something;}'
# ...or these (better)
sed '\#/a/b/c/#{do something;}'
sed '\_/a/b/c/_{do something;}'
sed '\%/a/b/c/%{do something;}'
#etc.
```


---

## Tagged mentions


