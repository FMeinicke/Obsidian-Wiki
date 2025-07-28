---
{"publish":true,"created":"2025-05-15T09:01:47.373+02:00","modified":"2025-05-26T15:25:05.465+02:00","published":"2025-05-26T15:25:05.465+02:00","cssclasses":""}
---

#gpg/full-gen-key

> [!info] Source
>
> - <https://withblue.ink/2020/05/17/how-and-why-to-sign-git-commits.html#generate-a-gpg-key-pair>

```shell
gpg --full-gen-key
```

Configure the key with:

1. Kind of key: type `4` for `(4) RSA (sign only)`
2. Keysize: `4096`
3. Expiration: choose a reasonable value, for example `2y` for 2 years ([[GPG/Create a key#Renew an expired key\|it can be renewed]])
4. Full Name
5. E-mail address ([[GPG/Create a key#Adding multiple E-mail addresses\|more can be added later]])

Type in a passphrase and you're done.