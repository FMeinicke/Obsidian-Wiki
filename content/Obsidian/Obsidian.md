---
publish: true
sorting-spec: |-
  Obsidian
  /:files
  /folders
cssclasses:
  - hide_properties
---

- [Callouts](Obsidian/Callouts.md)
- [Increase the Readable line length](Obsidian/Increase the Readable line length.md)

---


#obsidian/callouts

> [!info] Source
> 
> - <https://help.obsidian.md/Editing+and+formatting/Callouts>

- All possible callouts:

  > [!example]- Click to show
  >
  > > [!abstract]
  > > 
  > > ```markdown
  > > > [!abstract]
  > > > 
  > > > abstract
  > 
  > > [!summary]
  > > 
  > > ```markdown
  > > > [!summary]
  > > > 
  > > > summary
  > 
  > > [!tldr]
  > > 
  > > ```markdown
  > > > [!tldr]
  > > > 
  > > > tldr
  > 
  > > [!info]
  > > 
  > > ```markdown
  > > > [!info]
  > > > 
  > > > info
  > 
  > > [!todo]
  > > 
  > > ```markdown
  > > > [!todo]
  > > > 
  > > > todo
  > 
  > > [!tip]
  > > 
  > > ```markdown
  > > > [!tip]
  > > > 
  > > > tip
  > 
  > > [!hint]
  > > 
  > > ```markdown
  > > > [!hint]
  > > > 
  > > > hint
  > 
  > > [!important]
  > > 
  > > ```markdown
  > > > [!important]
  > > > 
  > > > important
  > 
  > > [!success]
  > > 
  > > ```markdown
  > > > [!success]
  > > > 
  > > > success
  > 
  > > [!check]
  > > 
  > > ```markdown
  > > > [!check]
  > > > 
  > > > check
  > 
  > > [!done]
  > > 
  > > ```markdown
  > > > [!done]
  > > > 
  > > > done
  > 
  > > [!question]
  > > 
  > > ```markdown
  > > > [!question]
  > > > 
  > > > question
  > 
  > > [!help]
  > > 
  > > ```markdown
  > > > [!help]
  > > > 
  > > > help
  > 
  > > [!faq]
  > > 
  > > ```markdown
  > > > [!faq]
  > > > 
  > > > faq
  > 
  > > [!warning]
  > > 
  > > ```markdown
  > > > [!warning]
  > > > 
  > > > warning
  > 
  > > [!caution]
  > > 
  > > ```markdown
  > > > [!caution]
  > > > 
  > > > caution
  > 
  > > [!attention]
  > > 
  > > ```markdown
  > > > [!attention]
  > > > 
  > > > attention
  > 
  > > [!failure]
  > > 
  > > ```markdown
  > > > [!failure]
  > > > 
  > > > failure
  > 
  > > [!fail]
  > > 
  > > ```markdown
  > > > [!fail]
  > > > 
  > > > fail
  > 
  > > [!missing]
  > > 
  > > ```markdown
  > > > [!missing]
  > > > 
  > > > missing
  > 
  > > [!danger]
  > > 
  > > ```markdown
  > > > [!danger]
  > > > 
  > > > danger
  > 
  > > [!error]
  > > 
  > > ```markdown
  > > > [!error]
  > > > 
  > > > error
  > 
  > > [!bug]
  > > 
  > > ```markdown
  > > > [!bug]
  > > > 
  > > > bug
  > 
  > > [!example]
  > > 
  > > ```markdown
  > > > [!example]
  > > > 
  > > > example
  > 
  > > [!quote]
  > > 
  > > ```markdown
  > > > [!quote]
  > > > 
  > > > quote
  > 
  > > [!cite]
  > > 
  > > ```markdown
  > > > [!cite]
  > > > 
  > > > cite


- The title can be changed by having text after the `[!callout]` part, e.g.

   > [!hint] A custom hint
   > 
   > ```markdown
   > > [!hint] A custom hint
   > > 
   > > This shows how to change the title of a callout.

- Callouts can also be foldable by adding a `+` or a `-` directly after `[!callout]` part, e.g.

   > [!question]- Can callouts be foldable?
   > 
   > ```markdown
   > > [!question]- Can callouts be foldable?
   > > 
   > > Yes, they can!

   > [!info]+ Behavior of the `+` and `-`
   > 
   > ```markdown
   > > [!info]+ Behavior of the `+` and `-`
   > > 
   > > The `+` expands the callout, the `-` collapses it.


#obsidian/css

> [!info] Source
> 
> - <https://www.reddit.com/r/ObsidianMD/comments/s55zcw/comment/hswuttk>
> - <https://gist.github.com/vii33/f2c3a85b64023cefa9df6420730c7531>

add a [CSS snippet](https://help.obsidian.md/Extending+Obsidian/CSS+snippets) with the following content
```css
:root {
    --custom_line_width: 1100px;
}

body {
    --file-line-width: var(--custom_line_width) /* !important */;
}
```

---

## Tagged mentions


