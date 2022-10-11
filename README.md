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

### Intro to Data types and operators
#### `-`, `+`, `/`, `*` 


### Comparison operators
- `>` greater than
- `<` less than
- `==` equal to
- `<=` less than or equal to
- `>=` more than or equal to
#### To commit multiple lines `ctrl+/`


```python
a = 24
b = 16
user_age = 18

print(a + b) # operator adds a to b
print(a - b) # operator minus b from a

#comparison

print(a>b) # True
print(a<b) # False
print(a==b) # False
```
```
### Boolean Builtin methods in Python - Boolean Methods
#### - DRY do not repeat yourself print("")
greeting = "Hello World!"
print(greeting)

#### These are some built in functions

# print(greeting.isalpha())
# print(greeting.islower())
# print(greeting.startswith("H"))  # check if it ends with specific letter
# print(greeting.isdigit())

# String Slicing
# string indexing - starts from 0]

# H e l l o W o r l d !
# 1 2 3 4 5 6 7 8 9 10 11
# we have built in methods to checks the len of string

print(len(greeting)) # prints 12
print(greeting[-1]) # prints !
print(greeting[0:5]) # prints Hello

print(greeting[-12:-6]) # prints Hello
print(greeting[-6:]) # prints World!

# String methods are available

white_space = "lot's of spaces at the end                                 "
# strip() removes the white spaces
print(len(white_space.strip())) # this removes all white spaces at the end

Example_text = "here's example text with lots of text"
print(Example_text.count("text")) # counts how many times text appears

print(Example_text.upper()) # capitalizes every letter
print(Example_text.capitalize()) # capitalizes the first letter
print(Example_text.replace("with", "'")) # replaces characters in string

```

```python
# user data input
first_name = "mohamed"
last_name = "yusuf"
salary =  40

print(first_name + " " + last_name + " " + str(salary)) # cast int to string using string()

# F-string
print(f"Hello {first_name} {last_name}")  # Python 3.5/6 or above

print("What is your name?")
name = input()

print("What is your DOB")
DOB = input()

print("Course Name?")
Course_name = input()

print("What is your door number?")
Door_number = str(input())

print("What is your address?")
address = input()

print("What are your hobbies?")
Hobby = input()

print(f"Hello my name is {name}, I was born on {DOB}, I am studying a {Course_name} course, I live in {Door_number} {address} and I enjoy {Hobby}")
```
## Data Collections

###  - Lists
### - Tuples
### - Dict



```python
# syntax list_name = ["adfsf", "asfdasd", "2sad23s"]
# apply DRY
# Lists
shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
shopping_list.append("chicken")
shopping_list[2]= "icecream" # add an item to the list
print(shopping_list)

shopping_list.pop() # removes the last item from list

# Can list have multiple data types
multiple_type = [1, 2, 3, "one", "five", "ten"]
print(multiple_type)
```
```python
# Tuples
# Immutable - cant be changed - edited - added
# user_details = DOB - country name - city name
# syntax ("")

essentials = ("milk", "paracetomol", "drinks")

print(essentials)
print(type(essentials))

```

