# Python intro
Python has become one of the most popular programming languages in the world in recent years. It's used in everything from machine learning to building websites and software testing. It can be used by developers and non-developers alike.
##  Why Python
Python language is incredibly easy to use and learn for new beginners and newcomers. The python language is one of the most accessible programming languages available because it has simplified syntax and not complicated

### Python use cases

Python has many use cases such as..
* Web Applications
* Data Science Implementations
* Artificial Intelligence
* Game Development
* Internet of things

### Python Variables

Variables are containers for storing data values.

 - Env Testing `print("hello world")`


```python
first_name = "Mohamed"
print(first_name)
name = input()
print("Hello " + name)
```
```python
# testing the env with print statement
# Dynamically typed language
# Python Variable?
# To store any data
# To store user data - hard code the data - any other 

print("What is your DOB?")
DOB = input()

print("Course Name?")
Course_name = input()

print("Are you a UK resident, Yes or No")
UK_resident = input()

```
### Github setup

Generate ssh key

```
cd /c/Users/stron
cd .ssh
ssh-keygen -t rsa -b 4096 -C "(your_email")
```

Create a repository on GitHub and follow the steps to connect to Pycharm

```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "git@github:[username]/[repository].git"
git push -u origin main
```


### Git & Github

- add changes to our Git-Hub repo - the changes that we made on local host

- `git add filename` or `git add` means push everything from current location
- `git commit -m "new markdown guide added`
- now let's send this new data to Github
- `git push -u origin main`
- `git status`


- To pull changes from Git-hub `git pull`

### Git cheat sheet

```These are common Git commands used in various situations:
start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```


