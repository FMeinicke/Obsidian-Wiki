---
publish: true
created: 2025-04-23T18:08:39.944+02:00
modified: 2025-05-26T17:02:45.000+02:00
published: 2025-05-26T17:02:45.000+02:00
---

#bash/random

> [!info] Source
>
> - <https://serverfault.com/a/1076250/600279>

```bash
START=5
LIMIT=42
echo $(( $START + $RANDOM % $LIMIT))
```

prints a random integer between 5 and 42
