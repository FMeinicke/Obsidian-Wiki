---
publish: true
created: 2025-05-15T09:01:46.373+02:00
modified: 2025-05-26T15:25:01.480+02:00
published: 2025-05-26T15:25:01.480+02:00
cssclasses: ""
---

#css/counter/steps

> [!info] Source
> 
> - <https://codepen.io/chriscoyier/pen/wvKeQOp>

```css
ol {
  list-style: none;
  counter-reset: steps;
}
ol li {
  counter-increment: steps;
}
ol li::before {
  content: counter(steps);
  margin-right: 0.5rem;
  background: #ff6f00;
  color: white;
  width: 1.2em;
  height: 1.2em;
  border-radius: 50%;
  display: inline-grid;
  place-items: center;
  line-height: 1.2em;
}
ol ol li::before {
  background: darkorchid;
}
```


---