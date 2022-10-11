
# Intro to Data types and operators
# - + * /


# Comparison operators
# - `>` greater than
# - `<` less than
# `==` True or False

# To commit multiple line `ctrl+/`

# a = 24
# b = 16
# user_age = 18
#
# print(a + b) # operator adds a to b
# print(a - b) # operator minus b from a
#
# # comparison
#
# print(a>b) # True
# print(a<b) # False
# print(a==b) # False


# Boolean Builtin methods in Python - Boolean Methods
# - DRY do not repeat yourself print("")

greeting = "Hello World!"
print(greeting)

# These are some built in functions
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


