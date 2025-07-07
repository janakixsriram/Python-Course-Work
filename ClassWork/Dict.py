student = {
"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student)

#Dictionary Operations
#Accessing Values

print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 21

#Adding and Updating Items
student["age"] = 22 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair
print(student)

#Removing Items from a Dictionary
#Using pop(key)
age = student.pop("age")
print(age) # Output: 22
print(student)

#Using del

del student["course"]
print(student)

#Using popitem()

student.popitem()
print(student)

#Using clear()

student.clear()
print(student) # Output: {}




