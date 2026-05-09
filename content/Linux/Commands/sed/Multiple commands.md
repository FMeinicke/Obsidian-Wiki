---
publish: true
created: 2024-12-06T06:58:21.490+01:00
modified: 2025-05-26T17:03:28.000+02:00
published: 2025-05-26T17:03:28.000+02:00
---

#sed

> [!info] Source

- simply concatenate the commands with `;`

  ```shell
  sed -n 's/\.//g;s/!define VERSION //p' "${0%/*}/setup.nsi"
  ```

- alternatively you could use multiple `-e`'s

  ```shell
  sed -n -e 's/\.//g' -e 's/!define VERSION //p' "${0%/*}/setup.nsi"
  ```

- the `-n` option causes `sed` to only output changed lines (in combination with the `p` command at the end)
