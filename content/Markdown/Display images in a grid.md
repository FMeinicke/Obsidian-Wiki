---
publish: true
created: 2024-12-06T06:58:22.223+01:00
modified: 2025-05-26T17:03:35.000+02:00
published: 2025-05-26T17:03:35.000+02:00
---

#image #grid

> [!info] Source

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
