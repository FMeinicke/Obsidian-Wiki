---
publish: true
created: 2024-12-06T06:58:17.204+01:00
modified: 2025-05-26T17:02:57.000+02:00
published: 2025-05-26T17:02:57.000+02:00
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
