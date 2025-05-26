---
publish: true
sorting-spec: |-
  Markdown
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Circled numbers](Markdown/Circled numbers.md)
- [Display images in a grid](Markdown/Display images in a grid.md)
- [Force a page break in a PDF export](Markdown/Force a page break in a PDF export.md)

---


#circled-numbers

> [!info] Source
>
>

- Unicode 0x2776 (=1) bis 0x277F (=10) und 0x24EB (=11) bis 0x24F4 (=20) und 0x24FF (=0)

  ```markdown
  &#x2776; <!-- circled 1 -->
  <font color="red">&#x2776;</font> <!-- red circled 1 -->
  ```

<font>&#x2776;</font> <!-- circled 1 -->
<font color="red">&#x2776;</font> <!-- red circled 1 -->


#image #grid

> [!info] Source
>
>

- controlled via the `width` of the `<img>`s
- important: `float: left;` CSS
- `margin`, so that the images don't just clamp together (order is `top` `right` `bottom` `left` when using 4 values)
- ex. a 2x2 grid

  ```markdown
  <div style="display: inline-block;">
    <img src="img/2023-02-23_11h36_54.png" style="float: left; width: 49.3%; margin: 0.66% 0.66% 0 0;">
    <img src="img/2023-02-23_11h37_05.png" style="float: left; width: 49.3%; margin: 0.66% 0.66% 0 0;">
    <img src="img/2023-02-23_11h37_11.png" style="float: left; width: 49.3%; margin: 0.66% 0.66% 0 0;">
    <img src="img/2023-02-23_11h37_16.png" style="float: left; width: 49.3%; margin: 0.66% 0.66% 0 0;">
    <img src="img/2023-02-23_11h37_22.png" style="float: left; width: 49.3%; margin: 0.66% 0.66% 0 0;">
  </div>
  ```


#markdown/page-break #div/style #css/page-break-after

> [!info] Source
> 
> - old Markdown documents; can't remember original source, probably SO

```markdown
This is some text which should be split on multiple pages.

<div style='page-break-after: always;'></div>

This appears on a new page.
```

---

## Tagged mentions


