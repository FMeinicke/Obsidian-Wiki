---
{"publish":true,"cssclasses":""}
---

#gpg/renew #gpg/edit-key #gpg/expire #gpg/trust

> [!info] Source
>
> <https://gist.github.com/krisleech/760213ed287ea9da85521c7c9aac1df0>

```shell
gpg --edit-key KEYID
```

In the GPG prompt:

```shell
gpg> expire
```

Now choose a new expiry date (e.g. `2y` for 2 years)

Optionally, do this for all subkeys (the primary key is `0`):

```shell
gpg> key 1
gpg> key 2
...
gpg> expire
```

Since the key has changed it needs to be trusted again:

```shell
gpg> trust
```

Finally, save the changes:

```shell
gpg> save
```

Then, [[GPG/Renew an expired key#Export public and private keys\|export the key again]] and [[GPG/Renew an expired key#Publish a key to a key server\|publish it to a key server]].