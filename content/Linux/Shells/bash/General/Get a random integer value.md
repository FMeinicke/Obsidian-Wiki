---
{"publish":true,"cssclasses":""}
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
