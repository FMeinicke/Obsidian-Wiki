---
publish: true
created: 2025-01-13T18:07:02.542+01:00
modified: 2025-05-26T17:02:14.000+02:00
published: 2025-05-26T17:02:14.000+02:00
---

#arch/pacman #archlinux-keyring #gpg

> [!info] Source
>
> - <https://wiki.archlinux.org/title/Pacman#.22Failed_to_commit_transaction_.28invalid_or_corrupted_package.29.22_error>
> - <https://wiki.archlinux.org/title/Pacman/Package_signing#Upgrade_system_regularly>

```shell
$ sudo pacman -Sy --needed archlinux-keyring
```

- then try to upgrade as usual
