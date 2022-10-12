# What is a Dictionary - Data collection type
# How to manage Dictionaries - How to manage the data using Dict
# It works as key value key - value
# Syntax { "name" : "Sparta"       }

# store student's data - name, course_name, progress, completed_lessons

student_1 = {
    "key" : "values",
    "name": "Mohamed",
    "stream" : "DevOps",
    "completed_lessons" : 4,
    "completed_lessons_names": ["lists", "tuples", "OOP"]

}

print(student_1)
print(student_1["stream"]) # This will display the value saved inside stream

# print/display completed_lessons_names
# print/display completed_lessons_names index 0 means lists

print(student_1["completed_lessons"])
print(student_1["completed_lessons_names"][0])

student_1["completed_lessons"] = 3 # change values in
print(student_1["completed_lessons"])

# Delete an item from the list of completed_lessons_name/key

student_1["completed_lessons_names"].remove("OOP")
print(student_1["completed_lessons_names"])

# Dict Builtin Methods
# display keys only or values

print(student_1.keys())
print(student_1.values())



