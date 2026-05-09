---
publish: true
created: 2025-03-24T17:55:21.366+01:00
modified: 2025-05-26T17:03:16.000+02:00
published: 2025-05-26T17:03:16.000+02:00
---

#openssl/enc #aes #key

> [!info] Source
>
> - <https://www.ibm.com/docs/en/imdm/12.0?topic=encryption-generating-aes-keys-password>

```console
$ openssl enc -aes-128-cbc -k secret -P -md sha1
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
salt=B85E4B947246274D
key=37F3D028910EC35FB956219FE487DFC8
iv =2015992ADD4263EE169084C6FD8C1FBA
```

- a valid AES key can also be generated using [[Generate a random string|a random string generated with openssl]]
