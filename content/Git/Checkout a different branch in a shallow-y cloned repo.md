---
{"publish":true,"created":"2025-05-15T09:01:47.623+02:00","modified":"2025-05-26T15:25:03.746+02:00","published":"2025-05-26T15:25:03.746+02:00","cssclasses":""}
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