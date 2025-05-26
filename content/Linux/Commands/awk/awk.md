---
publish: true
sorting-spec: |-
  awk
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Count from the end](Linux/Commands/awk/Count from the end.md)

---



#awk/print #awk/nf

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/64674/482223>

```shell
echo "This is a test" | awk '{ print$(NF-2) }'
is
```

---

## Tagged mentions


