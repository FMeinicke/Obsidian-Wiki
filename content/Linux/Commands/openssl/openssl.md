---
publish: true
sorting-spec: |-
  openssl
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Generate a random string](Linux/Commands/openssl/Generate a random string.md)
- [Generate AES key](Linux/Commands/openssl/Generate AES key.md)

---



#openssl/rand/-hex #openssl/rand/-base64 #random #password

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/306107/482223>

```shell
openssl rand -hex 20
# or
openssl rand -base64 20
```




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


---

## Tagged mentions


