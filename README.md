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