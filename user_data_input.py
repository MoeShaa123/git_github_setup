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


print("What is your adress?")
address = input()

print("What are your hobbies?")
Hobby = input()

print(f"Hello my name is {name}, I was born on {DOB}, I am studying a {Course_name} course, I live in {Door_number} {address} and I enjoy {Hobby}")
