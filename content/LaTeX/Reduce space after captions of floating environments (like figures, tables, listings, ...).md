---
{"publish":true,"created":"2025-05-15T09:01:49.060+02:00","modified":"2025-05-26T15:25:07.309+02:00","published":"2025-05-26T15:25:07.309+02:00","cssclasses":""}
---

#latex/caption #latex/spacing #latex/floats #latex/figure #latex/table #latex/listing #latex/setlength #latex/belowcaptionskip #latex/textfloatsep

> [!info] Source
> 
> - <https://tex.stackexchange.com/a/23315/239888>
> - <https://tex.stackexchange.com/a/23316/239888>

```latex
% in the preamble

% default: 0pt
\setlength{\belowcaptionskip}{-10pt}
% default: 20.0pt plus 2.0pt minus 4.0pt
\setlength{\textfloatsep}{10.0pt plus 2.0pt minus 4.0pt}
```

- note that the `\belowcaptionskip` also affects the space between subcaptions and the main caption, so setting this too small could squash these too close together and might look ugly