---
{"publish":true,"created":"2025-05-15T09:01:50.514+02:00","modified":"2025-05-26T15:25:10.872+02:00","published":"2025-05-26T15:25:10.872+02:00","cssclasses":""}
---


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