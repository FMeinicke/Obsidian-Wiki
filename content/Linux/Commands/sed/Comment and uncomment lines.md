---
{"publish":true,"cssclasses":""}
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