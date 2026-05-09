---
publish: true
created: 2025-03-08T16:46:37.145+01:00
modified: 2025-05-26T17:02:29.000+02:00
published: 2025-05-26T17:02:29.000+02:00
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
