# GIT
## What is version control?
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

## What is Git?
GIT is a distributed version control system. It is a tool to manage source code history. It allows you to track changes in your files, revert changes, and work simultaneously on multiple versions of your files.

## What is GitHub?
GitHub is a web-based hosting service for version control using Git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.

## What is the difference between Git and GitHub?
Git is a version control system that lets you manage and keep track of your source code history. GitHub is a cloud-based hosting service that lets you manage Git repositories.

## GITHUB REPOSITORY
A GitHub repository can be used to store a development project. It can contain folders and any type of files (HTML, CSS, JavaScript, Documents, Data, Images). A GitHub repository should also include a licence file and a README file about the project.


## INSTALLATION & GUIS
With platform specific installers for Git, GitHub also provides the ease of staying up-to-date with the latest releases of the command line tool while providing a graphical user interface for day-to-day interaction, review, and repository synchronization.
### GitHub for Windows
https://windows.github.com
### GitHub for Mac
https://mac.github.com
### For Linux and Solaris platforms, the latest release is available on the official Git web site.
### Git for All Platforms
https://git-scm.com

## SETUP
Configuring user information used across all local repositories

```bash
git config --global user.name “[firstname lastname]”
```
set a name that is identifiable for credit when review version history

```bash
git config --global user.email “[valid- ]”
```
set an email address that will be associated with each history marker

```bash
git config --global color.ui auto
```
set automatic command line coloring for Git for easy reviewing

# GIT COMMANDS
## SETUP & INIT
Configuring user information, initializing and cloning repositories
### git init
Initialize an existing directory as a Git repository
```bash
git init
```

### git clone
This command is used to obtain a repository from an existing URL.
```bash
git clone [url]
```





## STAGE & SNAPSHOT
Working with snapshots and the Git staging area

```bash
git status
```
show modified files in working directory, staged for your next commit

```bash
git add [file]
```
add a file as it looks now to your next commit (stage)

```bash
git reset [file]
```
unstage a file while retaining the changes in working directory

```bash
git diff
```
diff of what is changed but not staged

```bash
git diff --staged
```
diff of what is staged but not yet commited

```bash
git commit -m “[descriptive message]”
```
commit your staged content as a new commit snapshot



## BRANCH & MERGE
Isolating work in branches, changing context, and integrating changes
```bash
git branch
```
list your branches. a * will appear next to the currently active branch
    
```bash
git branch [branch-name]
```
create a new branch at the current commit
```bash
git checkout
```
switch to another branch and check it out into your working directory
```bash
git merge [branch]
```
merge the specified branch’s history into the current one

```bash
git log
```
show all commits in the current branch’s history


## INSPECT & COMPARE
Examining logs, diffs and object information
```bash
git log
```
show the commit history for the currently active branch
```bash
git log branchB..branchA
```
show the commits on branchA that are not on branchB
```bash
git log --follow [file]
```
show the commits that changed file, even across renames
```bash
git diff branchB...branchA
```
show the diff of what is in branchA that is not in branchB
```bash
git show [SHA]
```
show any object in Git in human-readable format


## TRACKING PATH CHANGES
Versioning file removes and path changes
```bash 
git rm [file]
```
delete the file from project and stage the removal for commit
```bash
git mv [existing-path] [new-path]
```
change an existing file path and stage the move
```bash
git log --stat -M
```
show all commit logs with indication of any paths that moved


## IGNORING PATTERNS
Preventing unintentional staging or commiting of files
```bash
git config --global core.excludesfile [file]
```
system wide ignore patern for all local repositories
```bash
logs/
*.notes
pattern*/
```
Save a file with desired paterns as .gitignore with either direct


## SHARE & UPDATE
Retrieving updates from another repository and updating local repos
```bash
git remote add [alias] [url]
```
add a git URL as an alias
```bash
git fetch [alias]
```
fetch down all the branches from that Git remote
```bash
git merge [alias]/[branch]
```
merge a remote branch into your current branch to bring it up to date
```bash
git push [alias] [branch]
```
Transmit local branch commits to the remote repository branch
```bash
git pull
```
fetch and merge any commits from the tracking remote branch


## REWRITE HISTORY
Rewriting branches, updating commits and clearing history
```bash
git rebase [branch]
```
apply any commits of current branch ahead of specified one
```bash
git reset --hard [commit]
```
clear staging area, rewrite working tree from specified commit


## TEMPORARY COMMITS
Temporarily store modified, tracked files in order to change branches
```bash
git stash
```
Save modified and staged changes
```bash
git stash list
```
list stack-order of stashed file changes
```bash
git stash pop
```
write working from top of stash stack
```bash
git stash drop
```
discard the changes from top of stash stack