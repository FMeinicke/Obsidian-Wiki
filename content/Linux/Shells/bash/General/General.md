---
publish: true
sorting-spec: |-
  General
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Divide variables](Linux/Shells/bash/General/Divide variables.md)
- [Escape single quotes inside single quotes](Linux/Shells/bash/General/Escape single quotes inside single quotes.md)
- [Get a random integer value](Linux/Shells/bash/General/Get a random integer value.md)
- [Move cursor to start of line to print over the line](Linux/Shells/bash/General/Move cursor to start of line to print over the line.md)
- [no-op](Linux/Shells/bash/General/no-op.md)
- [Print variable name and value](Linux/Shells/bash/General/Print variable name and value.md)

---



#bash/echo #bash/expansion

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/397588/482223>

```shell
$ VAR="foo"
$ echo ${VAR@A}
VAR='foo'
$ export VAR
$ echo ${VAR@A}
declare -x VAR='foo'
```



#bash/echo #cursor

> [!info] Source
> 
> - <https://stackoverflow.com/a/48319595/12780516>

- if we don't want to print new lines in a loop, for example, we can print over the same line again simply by appending `\r` at the end of the string we print and use `echo -ne`:

```shell
while $(ps aux | grep app:update >/dev/null ); do echo -ne "$(date): Waiting...\r"; sleep 2; done; echo -e "$(date): Done!          "
```

will print the current date and time followed by `: Waiting...` and will be refreshed every 2 seconds  
after it's done, it'll print the current time followed by `: Done!` (note the additional spaces, they're needed to overwrite the `Waiting...` completely since this is a longer string than `Done!`)



#bash/echo #bash/escaping #bash/quotes

> [!info] Source
> 
> - <https://stackoverflow.com/a/1250279/12780516>

- use double quotes to "escape" one single quote after ending the single quoted string and before starting the next part of the single quoted string

```shell
$ echo 'this is a single quote '"'"' inside a single quoted string'
this is a single quote ' inside a single quoted string
```

---



#bash/arithmethic-expression #linux/bc

> [!info] Source
> 
> - <https://stackoverflow.com/a/30398152/12780516>

- using an arithmetic expression (`$(( $a / $b ))`) only gives an integer result
- use `bc` for proper floating point math

```shell
a=100
b=42
echo $a / $b = $(bc <<<"scale=2; $a / $b")
```




#bash/while #bash/loop #bash/no-op

> [!info] Source
> 
> - <https://stackoverflow.com/a/44970525/12780516>

- a no-op (e.g., in a loop) is done with a colon (`:`) instead of an empty loop body

```bash
while true; do
    :
done
```




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


---

## Tagged mentions


