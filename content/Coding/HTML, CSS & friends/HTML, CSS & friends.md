---
{"publish":true,"cssclasses":"hide_properties"}
---


- [Hide element but keep space](Coding/HTML, CSS & friends/Hide element but keep space.md)
- [Ordered list with circled numbers](Coding/HTML, CSS & friends/Ordered list with circled numbers.md)

---


#css/visibility

> [!info] Source
> 
> - <https://stackoverflow.com/a/16316447/12780516>

```css
.hidden {
    visibility: hidden;
}
```


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

---

## Tagged mentions


