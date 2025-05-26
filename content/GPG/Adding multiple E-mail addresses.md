---
{"publish":true,"cssclasses":""}
---

#gpg/edit-key #gpg/trust

> [!info] Source
>
> - <https://withblue.ink/2020/05/17/how-and-why-to-sign-git-commits.html#adding-multiple-emails>

```shell
gpg --edit-key KEYID
```

In the GPG prompt:

```shell
gpg> adduid
```

Again, give it the full name and e-mail address.

Now, trust the new identity:

```shell
gpg> uid 2
gpg> trust
#Type "5" (for "I trust ultimately")
```

Finally, save the changes:

```shell
gpg> save
```

Repeat for as many e-mail addresses as needed.