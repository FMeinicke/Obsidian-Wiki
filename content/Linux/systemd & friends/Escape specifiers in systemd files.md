---
publish: true
created: 2025-04-23T18:08:39.937+02:00
modified: 2025-05-26T17:02:32.000+02:00
published: 2025-05-26T17:02:32.000+02:00
---

#systemd/specifier

> [!info] Source
>
> - <https://stackoverflow.com/a/54737279/12780516>
> - [`man systemd.unit`](https://man7.org/linux/man-pages/man5/systemd.unit.5.html#:~:text=use%20%22%25%25%22%20in%20place%20of%20%22%25%22)

- use `%%` i.e., `%%T` if you want to use `%T` as the format specifier for the `date` command instead of `%T` as the specifier for the temporary directory
