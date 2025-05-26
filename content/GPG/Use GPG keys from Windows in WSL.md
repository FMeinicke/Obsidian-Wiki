---
{"publish":true,"cssclasses":""}
---

#gpg/pinentry #windows

> [!info] Source
>
>

- Install `gpg`
- [[GPG/GPG#Import a key\|Import the GPG private key from Windows in WSL]] and trust it *ultimately*
- configure the WSL `gpg-agent` to use the Windows pinentry program for entering the passphrase --> create/edit `~/.gnupg/gpg-agent.conf` to contain

  ```shell
  # default-cache-ttl
  #   Set the time a cache entry is valid to n seconds. The default is 600
  #   seconds. Each time a cache entry is accessed, the entry’s timer is reset. To
  #   set an entry’s maximum lifetime, use max-cache-ttl.
  # 365 days
  default-cache-ttl 78840000

  # max-cache-ttl
  #   Set the maximum time a cache entry is valid to n seconds. After this time a
  #   cache entry will be expired even if it has been accessed recently or has
  #   been set using gpg-preset-passphrase. The default is 2 hours (7200 seconds).
  # 365 days
  max-cache-ttl 78840000

  pinentry-program /mnt/c/Program Files (x86)/Gpg4win/bin/pinentry.exe
  ```

---
publish: true
sorting-spec: |-
  Git
  common global settings
  /:files
  /folders
cssclasses:
  - hide_properties
---

> *It is easy to shoot your foot off with git, but also easy to revert to a previous foot and merge it with your current leg.*
> <span class="right-align">Jack William Bell</span>
> (from <https://mmapped.blog/posts/28-enlightenmentware#git>)

- [`fetch` results in error `fatal fetch-pack invalid index-pack output`](Git/`fetch` results in error `fatal fetch-pack invalid index-pack output`.md)
- [`HEAD`](Git/`HEAD`.md)
- [Break commit into multiple commits](Git/Break commit into multiple commits.md)
- [change commit author](Git/change commit author.md)
- [change commit date](Git/change commit date.md)
- [Checkout a different branch in a shallow-y cloned repo](Git/Checkout a different branch in a shallow-y cloned repo.md)
- [CLI Graph](Git/CLI Graph.md)
- [common global settings](Git/common global settings.md)
- [Delete a tag on a remote](Git/Delete a tag on a remote.md)
- [Disable SSL verification](Git/Disable SSL verification.md)
- [Fetch large commit history without every blob](Git/Fetch large commit history without every blob.md)
- [Fix `git gc` error `fatal bad tree object`](Git/Fix `git gc` error `fatal bad tree object`.md)
- [Ignore everything except subdirectory](Git/Ignore everything except subdirectory.md)
- [Keep committer date when rebasing](Git/Keep committer date when rebasing.md)
- [List all commits from a certain commit to the `HEAD`](Git/List all commits from a certain commit to the `HEAD`.md)
- [Location of custom scripts on Windows](Git/Location of custom scripts on Windows.md)
- [make file executable](Git/make file executable.md)
- [Mark a file as unchanged](Git/Mark a file as unchanged.md)
- [new empty branch](Git/new empty branch.md)
- [Organizing multiple git identities](Git/Organizing multiple git identities.md)
- [Push stashes to remote](Git/Push stashes to remote.md)
- [Quick Reference](Git/Quick Reference.md)
- [rebase on the 0-th commit](Git/rebase on the 0-th commit.md)
- [Recover a dropped stash or commit](Git/Recover a dropped stash or commit.md)
- [remove file from commit while rebasing](Git/remove file from commit while rebasing.md)
- [reset single file](Git/reset single file.md)
- [Set branch to certaincurrent commit without checking out that branch](Git/Set branch to certaincurrent commit without checking out that branch.md)
- [Temporarily switch editor](Git/Temporarily switch editor.md)
- [undo last commit](Git/undo last commit.md)
- [undo last rebase](Git/undo last rebase.md)
- [Use a different shell for `git submodule foreach`](Git/Use a different shell for `git submodule foreach`.md)
- [Use pre-commit hooks from Windows host in a devcontainer](Git/Use pre-commit hooks from Windows host in a devcontainer.md)

---



#git

> [!info] Source
> 
> - <https://beej.us/guide/bggit/html/split/quick-reference.html#quick-reference>

Quickly look up commands based on what you want to do! Caveat: this list is grotesquely incomplete! See your man pages for more info!

In this reference section we use the following substitutions:

- `URL`: Some URL either SSH, HTTP, or even a local file, usually the URL you cloned from.
- `FILE`: Path to file, e.g. `foo/bar.txt`, etc.
- `DIR`: Path to directory, e.g. `foo/`, etc.
- `PATH`: Path to directory or file
- `BRANCH`: Some branch name, e.g. `main`, etc.
- `REMOTE`: A remote name, e.g. `origin`, `upstream`, etc.
- `HASH`: Some commit hash - you can get a commit hash from `git log` or `git reflog`.
- `CMMT`: a commit hash, branch, etc. Anything that refers to a commit. Officially this is called a _tree-ish_, but that was more letters than I wanted to repeatedly type.
- `VARIABLE`: a Git config variable name, usually words separated by periods.
- `VALUE`: an arbitrary value for Git configs.
- `TAG`: a tag name

Also, don’t type the `---
publish: true
sorting-spec: |-
  Git
  common global settings
  /:files
  /folders
cssclasses:
  - hide_properties
---

> *It is easy to shoot your foot off with git, but also easy to revert to a previous foot and merge it with your current leg.*
> <span class="right-align">Jack William Bell</span>
> (from <https://mmapped.blog/posts/28-enlightenmentware#git>)

- [`fetch` results in error `fatal fetch-pack invalid index-pack output`](Git/`fetch` results in error `fatal fetch-pack invalid index-pack output`.md)
- [`HEAD`](Git/`HEAD`.md)
- [Break commit into multiple commits](Git/Break commit into multiple commits.md)
- [change commit author](Git/change commit author.md)
- [change commit date](Git/change commit date.md)
- [Checkout a different branch in a shallow-y cloned repo](Git/Checkout a different branch in a shallow-y cloned repo.md)
- [CLI Graph](Git/CLI Graph.md)
- [common global settings](Git/common global settings.md)
- [Delete a tag on a remote](Git/Delete a tag on a remote.md)
- [Disable SSL verification](Git/Disable SSL verification.md)
- [Fetch large commit history without every blob](Git/Fetch large commit history without every blob.md)
- [Fix `git gc` error `fatal bad tree object`](Git/Fix `git gc` error `fatal bad tree object`.md)
- [Ignore everything except subdirectory](Git/Ignore everything except subdirectory.md)
- [Keep committer date when rebasing](Git/Keep committer date when rebasing.md)
- [List all commits from a certain commit to the `HEAD`](Git/List all commits from a certain commit to the `HEAD`.md)
- [Location of custom scripts on Windows](Git/Location of custom scripts on Windows.md)
- [make file executable](Git/make file executable.md)
- [Mark a file as unchanged](Git/Mark a file as unchanged.md)
- [new empty branch](Git/new empty branch.md)
- [Organizing multiple git identities](Git/Organizing multiple git identities.md)
- [Push stashes to remote](Git/Push stashes to remote.md)
- [Quick Reference](Git/Quick Reference.md)
- [rebase on the 0-th commit](Git/rebase on the 0-th commit.md)
- [Recover a dropped stash or commit](Git/Recover a dropped stash or commit.md)
- [remove file from commit while rebasing](Git/remove file from commit while rebasing.md)
- [reset single file](Git/reset single file.md)
- [Set branch to certaincurrent commit without checking out that branch](Git/Set branch to certaincurrent commit without checking out that branch.md)
- [Temporarily switch editor](Git/Temporarily switch editor.md)
- [undo last commit](Git/undo last commit.md)
- [undo last rebase](Git/undo last rebase.md)
- [Use a different shell for `git submodule foreach`](Git/Use a different shell for `git submodule foreach`.md)
- [Use pre-commit hooks from Windows host in a devcontainer](Git/Use pre-commit hooks from Windows host in a devcontainer.md)

---

 - it’s the shell prompt. And everything after a `#` is a comment. A backslash `\` at the end of a line indicates that it continues on the next line.

## Glossary

- **Clone**: a duplicate (or to duplicate) a remote repo, commonly for local use.
- **Commit**: a snapshot of all the files in the repo at a point in time.
- **Fork**: a GitHub construct to make a clone of someone else’s GitHub repo under your GitHub account.
- **`HEAD`**: the commit that is currently checked out/switched to.
- **Index**: another name for the _stage_.
- **`main`**: the default name of the first branch created.
- **`master`**: the historical name for `main`.
- **`origin`**: the default name for the remote from which this repo was cloned.
- **Pull request**: a way to get changes you made in your fork of a repo back into the repo you forked from.
- **Remote**: an alias for a URL to another repo. Usually an HTTP or SSH URL.
- **Stage**: where you collect files to be bundled into a commit.
- **`upstream`**: the conventional name of the remote that you forked from. Not set up automatically.
- **Working Tree**: the collection of files you can see, which might have changes from the commit at `HEAD`.
- **WT**: shorthand for working tree.

## File States

- **Untracked** to:
    - Unmodified: `git add FILE`
- **Unmodified** to:
    - Modified: Edit with your editor and save
    - Untracked/deleted: `git rm --cached FILE`
- **Modified** to:
    - Staged: `git add FILE`
    - Unmodified: `git restore FILE` (discards changes)
    - Untracked/deleted: `git rm --cached FILE`
- **Staged**
    - Unmodified: `git commit FILE` (finalize commit)
    - Modified: `git restore --staged FILE` (unstage)
    - Both modified: `git checkout --merged FILE` (during merge)

## Configuration

For all `git config` commands, specify `--global` for a universal setting or leave it off to set the value just for this repo.

```shell
$ git config set VARIABLE VALUE
$ git config get VARIABLE
$ git config list
$ git config unset VARIABLE
$ git config --edit
```

### Set identity

Username and email:

```shell
$ git config set --global user.name "Your Name"
$ git config set --global user.email "your-email@example.com"
```

SSH identity:

```shell
$ git config set core.sshCommand \
    "ssh -i ~/.ssh/id_alterego_ed25519 -F none"
```

### Set default pull behavior to merge or rebase

```shell
$ git config set --global pull.rebase false   # Merge
$ git config set --global pull.rebase true    # Rebase
```

### Set default editor, difftool, and mergetool

Set the default editor to Vim, and the default mergetool and difftool to Vimdiff, turn off prompting for the tools, and turn off mergetool backups:

```shell
$ git config set core.editor vim
$ git config set diff.tool vimdiff
$ git config set difftool.prompt false
$ git config set difftool.vimdiff.cmd 'vimdiff "$LOCAL" "$REMOTE"'
$ git config set merge.tool=vimdiff
$ git config set mergetool.vimdiff.cmd \
                             'vimdiff "$LOCAL" "$REMOTE" "$MERGED"'
$ git config --global set mergetool.keepBackup false
```

### Colorful Git output

```shell
$ git config set color.ui true   # Or false
```

### Autocorrect

Autocorrect will automatically run the command it thinks you meant. For example, if you `git poush`, it will assume you meant `git push`.

```shell
$ git config set help.autocorrect 0   # Ask "Did you mean...?"
$ git config set help.autocorrect 7   # Wait 0.7 seconds before run

$ git config set help.autocorrect immediate  # Just guess and go
$ git config set help.autocorrect prompt     # Prompt then go
$ git config set help.autocorrect never      # Turn autocorrect off
```

### Newline translation

Handle automatic newline translation. Recommend set to true for Windows (not WSL) and false everywhere else.

```shell
$ git config set core.autocrlf true  # Windows (non-WSL)
$ git config set core.autocrlf false # WSL, Linux, Mac, C64, etc.
```

Obsolete commands for older versions:

```shell
git config user.email                     # Get
git config user.email "user@example.com"  # Set
git config --unset user.email             # Delete
git config --list                         # List
git config --edit                         # Edit
```

### Aliases

Setting aliases, some examples:

```shell
$ git config set --global alias.logn 'log --name-only'
$ git config set alias.aa "add --all"
$ git config set alias.logc "log --oneline --graph --decorate"
$ git config set alias.diffs "diff --staged"
$ git config set alias.lol "log --graph" \
  " --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s" \
  " %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

Getting aliases:

```shell
$ git config get alias.logx
$ git config get --all --show-names --regexp '^alias\.'
$ git config set alias.aliases \
    "config get --all --show-names --regexp '^alias\.'"
```

Tracing an alias run:

```shell
$ GIT_TRACE=1 git logx
```

## Creating and Cloning Repos

```shell
$ git clone URL       # Clone a URL
$ git clone URL DIR   # Clone a URL to directory
$ git init DIR        # Init repo at directory
$ git init .         # Init repo in the current directory
```

## Adding, Renaming, Deleting, Committing

```shell
$ git add PATH             # Add PATH to the repo
$ git mv FILE1 FILE2       # Rename ("Move") FILE1 to FILE2
$ git mv FILE2 FILE1       # Undo the above rename
$ git rm FILE              # Delete ("Remove") FILE
$ git add -p FILE          # Add file in patch mode

$ git commit               # Commit files on stage
$ git commit -m "message"  # Commit with a message
```

Amending commits - don’t amend commits you have pushed unless you know what you’re getting into!

```shell
$ git commit --amend               # Amend last commit
$ git commit --amend -m "message"  # Amend with commit message
$ git commit --amend --no-edit     # Don't change commit message
```

To undelete a staged file, run these two commands in sequence:

```shell
$ git restore --staged FILE
$ git restore FILE
```

To undelete a deleted file, you could manually recover it from an old commit, or revert the commit that deleted it.

## Getting Status

```shell
$ git status             # Show current file states
$ git log                # Show the commit logs
$ git log --name-only    # Also list changed files
$ git log CMMT           # Show log from a specific branch
$ git log CMMT1 CMMT2    # Show logs from multiple branches

$ git log CMMT1..CMMT2   # Show logs from CMMT2 since it
                         # diverged from CMMT1
$ git log CMMT1...CMMT2  # Show logs from CMMT1 and CMMT2
                         # since they diverged
```

## Getting a Diff

```shell
$ git diff                # Diffs between working tree and stage
$ git diff HEAD^          # Diff from the previous commit to here
$ git diff HEAD^^         # Diff from the 2nd last commit to here
$ git diff HEAD~3 HEAD~2  # Diff from 3rd last to 2nd last commit
$ git diff CMMT           # Diff between CMMT and now
$ git diff CMMT1 CMMT2    # Diff between two commits (older first)

$ git diff CMMT1...CMMT2  # Diff between CMMT2 and the common
                          # ancestor of CMMT1 and CMMT2

$ git diff HEAD~3^!       # Diff between HEAD~3 and its parent
$ git diff -- FILE        # Run a diff just for a specific file
$ git diff HEAD^ -- FILE  # Run a diff just for a specific file

$ git diff -U5          # Show 5 lines of context
$ git diff -w           # Ignore whitespace
$ git diff --name-only  # Only show filenames of changed files
$ git diff --staged     # Diffs between stage and repo
$ git difftool          # Diffs using the configured difftool
```

## Branches

A local branch looks like `branchname`. A remote tracking branch looks like `remote/branchname`.

```shell
$ git switch BRANCH         # Switch to a branch
$ git switch --detach HASH  # Detach HEAD to a commit
$ git switch -              # Switch back to previous commit
```

```shell
$ git switch --detach HEAD^   # Switch to previous commit
$ git switch --detach HEAD^^  # Switch to 2 commit ago
$ git switch --detach HEAD~3  # Switch to 3 commits ago
$ git switch --detach HEAD~99 # Switch to 99 commits ago
```

```shell
$ git switch main   # Reattach HEAD to main
```

```shell
$ git branch -v   # List all branches
$ git branch -va  # List all including remote tracking branches
```

```shell
$ git switch -c BRANCH        # Create and switch to BRANCH
$ git branch BRANCH           # Create BRANCH at HEAD
$ git branch BRANCH1 BRANCH2  # Create BRANCH1 at BRANCH2
```

```shell
$ git branch -d BRANCH   # Delete fully merged branch
$ git branch -D BRANCH   # Force delete unmerged branch
```

Obsolete style (use `switch` if you can):

```shell
$ git checkout CMMT      # Detach HEAD to a commit
$ git checkout HEAD^     # Detach HEAD to previous commit
$ git checkout HEAD~2    # Detach HEAD to second previous commit
```

## Pulling and Pushing, and Fetching

```shell
$ git pull               # Pull from remote and merge or rebase
$ git pull --ff-only     # Only allow fast-forward merges
$ git pull --rebase      # Force a rebase on pull
$ git pull --no-rebase   # Force a merge on pull
```

```shell
$ git push                     # Push this branch to its remote

$ git push REMOTE BRANCH       # Create remote tracking branch and
                               # push to remote

$ git push -u REMOTE BRANCH    # Create remote tracking branch and
                               # push to remote, and use subsequent
                               # `git push` commands for this local
                               # branch

$ git push -u origin branch99  # Example

$ git push --tags              # Push all tags to origin
$ git push REMOTE --tags       # Push all tags to specific remote
$ git push REMOTE tag3.14      # Push single tag
```

```shell
$ git fetch        # Get data from remote but don't merge or rebase
$ git fetch REMOTE # Same, for a specific remote
```

## Merging

```shell
$ git merge CMMT     # Merge commit or branch into HEAD
$ git merge --abort  # Rollback the current merge
$ git mergetool      # Run mergetool to resolve a conflict

$ git checkout --merged FILE   # Unstage resolved files
```

In a conflict occurs, you can always `--abort`. Otherwise:

1. Fix the conflict.
2. Add the fixed files.
3. Commit to complete the merge.

## Remotes

```shell
$ git remote -v                       # List remotes
$ git remote set-url REMOTE URL       # Change remote's URL
$ git remote add REMOTE URL           # Add a new remote
$ git remote rename REMOTE1 REMOTE2   # Rename REMOTE1 to REMOTE2
$ git remote remove REMOTE            # Delete REMOTE
```

## Ignoring Files

Add a `.gitignore` file to your repo. It applies to this directory and all non-submodule subdirectories below it. Add descriptions of files to ignore to this file. Comments behind `#` are allowed. Blank lines are ignored.

Example `.gitignore`:

```shell
foo.aux     # Ignore specific file "foo.aux"
foo.-     # Ignore all files that start with "foo."
*.tmp       # Ignore all files that end with ".tmp"
frotz/      # Ignore all files in the "frotz" directory
foo[12].txt # Ignore "foo1.txt" and "foo2.txt"
foo?        # Ignore "foo" followed by any single character
frotz/bar   # Ignore file "bar" in directory "frotz"
-         # Ignore everything
```

Exceptions to earlier rules, also useful in `.gitignore` files in subdirectories to override rules from parent directories:

```shell
*.txt       # Ignore all text files
!keep.txt   # Except "keep.txt"
```

## Rebasing

```shell
$ git rebase CMMT        # Rebase changes onto commit

$ git rebase -i CMMT     # Interactive rebase (squashing commits)

$ git rebase --continue  # Continue processing from conflict
$ git rebase --skip      # Skip a conflicting commit
$ git rebase --abort     # Bail out of rebasing
```

```shell
$ git pull --rebase      # Force a rebase on pull
$ git pull --no-rebase   # Force a merge on pull
```

## Stashing

Stashes are stored on a stack.

```shell
$ git stash push    # Stash changed files
$ git stash         # Effectively the same as "push"
$ git stash FILE    # Stash a specific file
$ git stash pop     # Replay stashed files on working tree
$ git stash list    # List stashed files

$ git stash pop 'stash@{1}'   # Pop stash at index 1
$ git stash pop --index 1     # Same thing
$ git stash drop 'stash@{1}'  # Drop stash at index 1
$ git stash drop --index 1    # Same thing
```

## Reverting

```shell
$ git revert CMMT     # Revert a specific commit
$ git revert -n CMMT  # Revert but don't commit (yet)

$ git revert CMMT1 CMMT2    # Revert multiple commits
$ git revert CMMT1^..CMMT2  # Revert a range (oldeest first)

$ git revert --continue  # Continue processing from conflict
$ git revert --skip      # Skip a conflicting commit
$ git revert --abort     # Bail out of reverting
```

## Resetting

All resets move `HEAD` and the current checked out branch to the specified commit.

```shell
$ git reset --mixed CMMT  # Set stage to CMMT, don't change WT
$ git reset CMMT          # Same as --mixed
$ git reset --soft CMMT   # Don't change stage or working tree
$ git reset --hard CMMT   # Set stage and WT to CMMT

$ git reset -p CMMT       # Reset file in patch mode
```

Obsolete usage:

```shell
$ git reset FILE   # Same as "git restore --staged FILE"
```

## The Reflog

```shell
$ git reflog      # Look at the reflog
```

...I admit this section could use a bit more information.

## Cherry-pick

```shell
$ git cherry-pick CMMT   # Cherry-pick a particular commit
```

## Blame

```shell
$ git blame FILE                # Who is responsible for each line
$ git blame --date=short FILE   # Same, shorter date format
```

## Submodules

```shell
$ git clone --recurse-submodules URL       # Clone with submodules
$ git submodule update --recursive --init  # If you cloned without

$ git submodule add URL              # Add submodule
$ git add DIR                        # Add to repo
$ git pull --recurse-submodules      # Pull including submodules

$ git submodule status               # Submodule status
$ git ls-tree HEAD DIR               # Show submod pinned commit
$ git submodule init                 # Set up bookeeeping
$ git submodule update               # Bring in missing submods
$ git submodule update --recursive   # Handle submods of submods
```

Deleting a submodule - do these in order. In this example, DIR is the name of the submodule directory.

```shell
$ git submodule deinit DIR
$ rm -rf .git/modules/DIR
$ git config -f .gitmodules --remove-section submodule.DIR
$ git add .gitmodules
$ git rm --cached DIR
$ git commit -m "remove DIR submodule"
```

## Tags

```shell
$ git tag     # List tags
$ git tag -l  # List tags
```

```shell
$ git tag TAG          # Create a tag on HEAD
$ git tag TAG CMMT     # Create a tag on a specific commit
$ git tag -a TAG       # Create an annotated tag
$ git tag -a TAG CMMT  # On a specific commit
$ git tag -a TAG -m "message" # Add a message to the tag
```

```shell
$ git push --tags          # Push all tags to origin
$ git push REMOTE --tags   # Push all tags to specific remote
$ git push REMOTE tag3.14  # Push specific tag
```

```shell
$ git tag -d tagname          # Delete a tag locally
$ git push REMOTE -d tagname  # Delete a tag on a remote
```



#git-config

> [!info] Source
>
> - <https://blog.gitbutler.com/how-git-core-devs-configure-git> (partly)

```ini
[core]
    autocrlf = true
    editor = code --wait
    # or for terminal-only
    #editor = vim
[user]
    name = Florian Meinicke
    email = florian.meinicke@cetoni.de
    signingKey = 6CA69321
[pull]
    rebase = true
[rebase]
    autoStash = true
    autoSquash = true
[init]
    defaultbranch = main
[commit]
    gpgSign = true
[tag]
    gpgSign = true
```

### Windows-specific

```ini
[core]
    # enable symlinks on Windows
    symlinks = true
    # use the Windows built-in ssh command instead of git's
    sshCommand = C:/Windows/System32/OpenSSH/ssh.exe
[credential]
    helper = manager-core
[gpg]
    program = C:\\Program Files (x86)\\Gpg4win\\..\\GnuPG\\bin\\gpg.exe
[http]
    # to allow connecting to servers via HTTPS w/ a self-signed certificate (Windows only)
    sslBackend = schannel
```

## Settings that even Git core developers change

```ini
# clearly makes git better

[column]
    ui = auto
[branch]
    sort = -committerdate
[tag]
    sort = version:refname
[init]
    defaultBranch = main
[diff]
    algorithm = histogram
    colorMoved = plain
    mnemonicPrefix = true
    renames = true
[push]
    default = simple
    autoSetupRemote = true
    followTags = true
[fetch]
    prune = true
    pruneTags = true
    all = true

# why the hell not?

[help]
    autocorrect = prompt
[commit]
    verbose = true
[rerere]
    enabled = true
    autoupdate = true
[core]
    excludesfile = ~/.gitignore
[rebase]
    autoSquash = true
    autoStash = true
    updateRefs = true

# a matter of taste (uncomment if you dare)

[core]
    # fsmonitor = true
    # untrackedCache = true
[merge]
    # (just 'diff3' if git version < 2.3)
    # conflictstyle = zdiff3 
[pull]
    # rebase = true
```



#git/head

> [!info] Source(s)
> 
> - 

| spec       | meaning                       |
| ---------- | ----------------------------- |
| `HEAD~2`   | 2 commits older               |
| `HEAD^2`   | second parent of merge commit |
| `HEAD@{2}` | third listing in reflog       |
| `HEAD~~`   | 2 commits older               |
| `HEAD^^`   | 2 commits older               |


#git/switch/orphan #git/branch/orphan

> [!info] Source
>
>

```shell
git switch --orphan new-branch
#or
git branch --orphan new-branch
```


#git/log/graph #git-graph #cli

> [!info] Source
>
>

```shell
git log --oneline --graph --decorate --all
```


#git/rebase/root

> [!info] Source
>
>

```shell
git rebase --root
```


#git/reset #git/rebase

> [!info] Source
>
>

```shell
git reset HEAD^ /path/to/file
```


#git/reflog #git/reset/hard #git/rebase

> [!info] Source
>
>

```shell
git reflog                   # find HEAD commit of the branch as it was before rebasing
git reset --hard "HEAD@{x}"  # where "HEAD@{x}" is the commit before rebasing
```


#git/update-index/add #git/update-index/chmod

> [!info] Source
>
>

```shell
git update-index --add --chmod=+x /path/to/file
```

- the `--add` causes the file to be staged if necessary


#git/checkout

> [!info] Source
>
>

```shell
git checkout HEAD -- /path/to/file
```


#git/init #git/fetch

> [!info] Source
>
>

```shell
git init   # reinitialize local repository
git fetch
```

otherwise maybe <https://stackoverflow.com/a/73079516/12780516>


#git/rebase

> [!info] Source
>
> - <https://stackoverflow.com/a/2976598/12780516>

```shell
git rebase --committer-date-is-author-date <REF>
```


#git-identities

> [!info] Source
>
> - <https://garrit.xyz/posts/2023-10-13-organizing-multiple-git-identities>


#git/tag

> [!info] Source
>
> - <https://stackoverflow.com/a/5480292/12780516>

```shell
git tag -d tagname && git push origin :tagname
```


#git/reset/soft #git/restore/staged

> [!info] Source
> 
> - <https://www.git-tower.com/learn/git/faq/undo-last-commit>

```shell
git reset --soft HEAD~             # keeps the files staged
git restore --staged <files...>    # unstages the files
git restore <files...>             # restores the files to before the commit
```


#git/commit

> [!info] Source
> 
> - <https://www.git-tower.com/learn/git/faq/change-author-name-email>

```shell
git commit --author "My Name <my_name@example.com>"
```


#git/update-index

> [!info] Source
> 
> - pwsh history

```shell
git update-index --assume-unchanged <FILE>
```

- to undo

```shell
git update-index --no-assume-unchanged <file>
```


#git/commit/amend #git/commit/date

> [!info] Source
> 
> - <https://stackoverflow.com/a/9110424/12780516>

```shell
git commit --amend --date "Thu Mar 21 2024 12:15:06 GMT+0100"
```

- date formats understood by git: <https://git-scm.com/docs/git-commit#_date_formats>


#git #ssl #no-verify

> [!info] Source
> 
> - <>

- set `GIT_SSL_NO_VERIFY=1`


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


#git/submodule/foreach #linux/sh #linux/bash #bash

> [!info] Source
> 
> - <https://stackoverflow.com/a/65086817/12780516>

- git uses `/bin/sh`, so we simply need to link this to our desired shell (e.g., `bash`)

```shell
sudo ln -sf bash /bin/sh
```


#git/log/format #git/log/reverse

> [!info] Source(s)
> 
> - shell history

```shell
git log --format=%H --reverse <commit hash>..HEAD > commits.txt
```


#git/script #git/bin #git/for-windows #windows

> [!info] Source
> 
> - <https://superuser.com/a/1688527/1201131>

- custom scripts go into `~/bin/` (i.e., `C:\Users\<User>\bin`)
- if the script is called `git-myscript`, then it can be called using `git myscript` from both Git Bash and any Windows shell (CMD/pwsh)


#git/stash #git/push #git/refs #git/fetch #git/rstash

> [!info] Source
> 
> - <https://stackoverflow.com/a/61356308/12780516>
> - <https://github.com/501st-alpha1/git-rstash>

- TL;DR: use `git-rstash` from [here](https://github.com/501st-alpha1/git-rstash)
    - stashes are pushed as commits to `refs/stashes/`
    - when `fetch`ing the local `refs/stashes/` will be populated and `import`ing a stash (or all stashes) converts the commits to stashes using `git stash --store`

```console
git rstash push-all                        # pushes all stashes
git rstash push 0                          # pushes stash 0
git rstash fetch && git rstash import-all  # fetches all stashes and populates the local stash with them
```



#git/commit #git/reset #git/rebase/interactive #git/rebase/edit

> [!info] Source
> 
> - <https://stackoverflow.com/a/6217314/12780516>

### Split the most recent commit

```shell
git reset HEAD~
```

- then commit the pieces individually as usual

### Split an older commit (during a rebase)

```shell
git rebase -i <commit-ish>
```

- in the rebase editor select `edit` for the commit to be split; save and close
- you should now be at the correct point in the commit history, so again

```shell
git reset HEAD~
```

- and again, commit the pieces individually as usual


#git/branch/force

> [!info] Source
> 
> - <https://stackoverflow.com/a/5471197/12780516>

```shell
git branch --force <branch-name> [<new-tip-commit>]
```

- without `<new-tip-commit>` this defaults to setting the branch to the current commit
- `<new-tip-commit>` can also be another branch name (e.g., `main`, `origin/main`)


#git/--filter #git/blob

> [!info] Source
> 
> - <https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/#user-content-partial-clone>

- use `--filter=blob:none` to only download the commits and trees

```shell
git clone --filter=blob:none <url>
# or
git fetch --filter=blob:none [options...]
```

- only when you then do a checkout of a certain commit, git will download the corresponding blobs for that commit



#git/GIT_EDITOR #git/editor

> [!info] Source
> 
> - <https://www.reddit.com/r/git/comments/7mh49p/is_there_a_way_to_switch_text_editors_temporarily/>

- use `GIT_EDITOR=<editor>`, e.g.

```shell
GIT_EDITOR=vim git rebase -i ...
```


#git/fetch/--refetch #git/gc/--aggressive

> [!info] Source
> 
> - <https://stackoverflow.com/a/74286404/12780516>

- this error might happen during a `git fetch`:

```shell
git fetch
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
warning: The last gc run reported the following. Please correct the root cause
and remove .git/gc.log
Automatic cleanup will not be performed until the file is removed.

fatal: bad tree object 9213e6d7ad31bde664dd103745302c3750cbecbd
fatal: failed to run repack
```

- it can be resolved by running

```shell
git fetch --refetch
git gc --aggressive
```



#git/stash/apply #git/gitk #git/fsck #awk #pwsh/select-string #pwsh/foreach 

> [!info] Source
> 
> - <https://stackoverflow.com/a/91795/12780516>

- to find the dropped stash / all unreferenced commits ever

```shell
gitk --all $( git fsck --no-reflog | awk '/dangling commit/ {print $NF}' )
```

- or on Windows

```powershell
gitk --all $( git fsck --no-reflog | select-string 'dangling commit' | foreach { $_.ToString().Split(" ")[-1] } )
```

- then look for *WIP on somebranch* or *autostash* commit messages
- once found, note the commit hash
- to apply the stash run

```shell
git stash apply $stash_hash
```




#ls/-al #bash/for #ls/-1 #cat/-v #line-endings #line-endings/crlf #line-endings/lf #tr/-d

> [!info] Source
> 
> - <https://stackoverflow.com/a/77198331/12780516>

- ensure that the hooks are executable and contain Linux line endings (LF instead of CRLF)

```shell
ls -al .git/hooks/
for f in $(ls -1 .git/hooks/* | grep -v '.sample'); do cat -v ${f}; done
```

(look for `^M` sequences in the `cat` output -> this means that the file has Windows CRLF line endings)

- to convert all hooks

```shell
for f in $(ls -1 .git/hooks/* | grep -v '.sample'); do cat -v ${f} | tr -d '\r' > ${f}.tmp && mv ${f}.tmp ${f}; done
```

(see [[Linux/Commands/ls with path\|ls with path]])



#git/gitignore

> [!info] Source
> 
> - <https://stackoverflow.com/a/8594971/12780516>

```gitingore
/*
/*/
!/<DIRECTORY>
```


---

## Tagged mentions


