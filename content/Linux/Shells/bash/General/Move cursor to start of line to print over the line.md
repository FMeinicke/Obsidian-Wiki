---
publish: true
created: 2025-05-15T09:01:50.576+02:00
modified: 2025-05-26T15:25:11.091+02:00
published: 2025-05-26T15:25:11.091+02:00
cssclasses: ""
---


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