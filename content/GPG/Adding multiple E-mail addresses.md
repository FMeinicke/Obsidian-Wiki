---
publish: true
created: 2024-12-06T06:58:21.154+01:00
modified: 2025-05-26T17:03:25.000+02:00
published: 2025-05-26T17:03:25.000+02:00
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
