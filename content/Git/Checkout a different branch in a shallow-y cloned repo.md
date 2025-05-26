---
{"publish":true,"cssclasses":""}
---

#git/clone/depth #git/fetch/depth #git/reset/hard

> [!info] Source
> 
> - ChatGPT conversation

```shell
# assume the repo was cloned with
git clone --depth=1 -b main <URL> <PATH>

# to update 'main' we can do
git fetch --depth=1 origin main
git reset --hard origin/main

# to reset the local state to a different branch than 'main'
git fetch --depth=1 origin <BRANCH>
git reset --hard FETCH_HEAD
```

- this same procedure can be applied to the 'main' branch, as well, i.e., if `<BRANCH>` is `main`