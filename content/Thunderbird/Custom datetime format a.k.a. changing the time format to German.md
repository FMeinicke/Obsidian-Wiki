---
publish: true
created: 2024-12-06T06:58:10.344+01:00
modified: 2025-05-27T08:42:10.000+02:00
published: 2025-05-27T08:42:10.000+02:00
---

#thunderbird/date_time_format #thunderbird/date_format #thunderbird/time_format #thunderbird/advanced_preferences #thunderbird/locale/german

> [!info] Source(s)
>
> - <https://support.mozilla.org/en-US/kb/customize-date-time-formats-thunderbird#w_create-date-and-time-format-override-preferences-using-thunderbirds-config-editor>

- open the **Advanced Preferences** and create a new string variable called `intl.date_time.pattern_override.time_short` and set it to `HH:mm` to display the time in 24-hour format
- to change the date format to `dd.MM.yyyy` create and set the string variable `intl.date_time.pattern_override.date_short`
