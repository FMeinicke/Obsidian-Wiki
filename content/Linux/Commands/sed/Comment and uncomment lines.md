---
{"publish":true,"created":"2025-05-15T09:01:49.654+02:00","modified":"2025-05-26T15:25:08.638+02:00","published":"2025-05-26T15:25:08.638+02:00","cssclasses":""}
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