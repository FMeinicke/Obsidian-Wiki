---
publish: true
created: 2025-05-15T09:01:49.561+02:00
modified: 2025-05-26T15:25:08.481+02:00
published: 2025-05-26T15:25:08.481+02:00
cssclasses: ""
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

- a valid AES key can also be generated using [[Linux/Commands/openssl/Generate a random string\|a random string generated with openssl]]
