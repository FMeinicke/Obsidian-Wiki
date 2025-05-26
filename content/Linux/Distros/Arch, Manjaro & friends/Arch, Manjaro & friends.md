---
publish: true
sorting-spec: |-
  Arch, Manjaro & friends
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Boost 1.74 libs](Linux/Distros/Arch, Manjaro & friends/Boost 1.74 libs.md)
- [Fix _invalid or corrupted packages_ error](Linux/Distros/Arch, Manjaro & friends/Fix _invalid or corrupted packages_ error.md)
- [Install new CA certificates](Linux/Distros/Arch, Manjaro & friends/Install new CA certificates.md)

---



#boost/1-74 #yay

> [!info] Source(s)
> 
> - <https://forum.manjaro.org/t/question-about-boost-libs-1-74-0-and-vpn-unlimited/143731/4?u=fmeinicke>

- available in the AUR

```shell
yay -S boost174-libs
```



#trust/anchor/--store #certificate #ca-certificate

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/422372/482223>

```shell
sudo trust anchor --store path/to/certificate.crt
```



#arch/pacman #archlinux-keyring #gpg

> [!info] Source
> 
> - <https://wiki.archlinux.org/title/Pacman#.22Failed_to_commit_transaction_.28invalid_or_corrupted_package.29.22_error>
> - <https://wiki.archlinux.org/title/Pacman/Package_signing#Upgrade_system_regularly>

```shell
$ sudo pacman -Sy --needed archlinux-keyring
```

- then try to upgrade as usual


---

## Tagged mentions


