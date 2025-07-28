---
{"publish":true,"created":"2025-05-15T09:01:47.529+02:00","modified":"2025-05-26T15:25:05.903+02:00","published":"2025-05-26T15:25:05.903+02:00","cssclasses":""}
---

#gpg/gen-revoke #gpg/send-keys

> [!info] Source
>
> - <https://askubuntu.com/a/626549>
> - <https://askubuntu.com/a/323309>
> - <https://askubuntu.com/a/523361>

- Generate a revocation certificate

  ```shell
  gpg --output <user>.<name>.revoke.asc --gen-revoke KEYID
  ```

- Import the revocation certificate (**Note: This requires the public key to be present! If this is not the case yet, simply pull it from a server using `gpg --recv-keys KEYID`.**)

  ```shell
  gpg --import <user>.<name>.revoke.asc
  ```

- Then send the key back to the server again

  ```shell
  gpg --keyserver keyserver.ubuntu.com --send-keys KEYID
  ```