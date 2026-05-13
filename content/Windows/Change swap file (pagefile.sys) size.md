---
publish: true
created: 2025-05-15T09:01:51.561+02:00
modified: 2025-05-27T08:42:35.497+02:00
published: 2025-05-27T08:42:35.497+02:00
cssclasses: ""
---

#windows/pagefile #windows/swap #swap #ram

> [!info] Source
> 
> - <https://superuser.com/a/793325/1201131>

- press <kbd>Win</kbd>+<kbd>R</kbd> to bring up the command runner and enter `systempropertiesadvanced.exe`, then press <kbd>Enter</kbd>
- in the dialog that opened go to the **Advanced** tab, then under *Performance* click *Settings...*
- in the next dialog go to the **Advanced** tab again, and under *Virtual Memory* click *Change...*
- in that dialog select a drive for where to store the swap file (you can have multiple files on different drives) and enter the desired minimum and maximum sizes, or let Windows decide
- when you're done, click *Set*, then *OK*, followed by two more *OK*s for the other two dialogs to close everything

---