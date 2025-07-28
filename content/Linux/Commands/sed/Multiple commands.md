---
{"publish":true,"created":"2025-05-15T09:01:49.686+02:00","modified":"2025-05-26T15:25:08.684+02:00","published":"2025-05-26T15:25:08.684+02:00","cssclasses":""}
---


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