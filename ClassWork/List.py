# 1.empty the list

list = []  # Empty list
name = [34,234,2]
print(name)

# 2.List with Elements

numbers = [1, 2, 3, 4, 5] # List of integers
fruits = ["apple", "banana", "cherry"] # List of strings
mixed = [10, "Python", 3.14, True] # Mixed data types
print(numbers)
print(fruits)
print(mixed)

# 3.List with Nested Lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)


# Using Indexing (Positive & Negative)

my_list = ["Python", "Java", "C++"]
print(my_list[0]) # Python
print(my_list[1]) # Java
print(my_list[-1]) # C++ (Negative Indexing)

# Using Slicing

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30] (from start)
print(numbers[2:]) # [30, 40, 50] (to end)
print(numbers[-3:-1]) # [30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10] (Reverse list)

 
# Changing Elements

numbers = [10, 20, 30, 40]
print(numbers[2]) # 100
print(numbers) # [10, 20, 100, 40]

#Adding Elements

# Append (adds to the end)
print(numbers.append(50))
# Insert (adds at a specific position)
print(numbers.insert(1, 15))
# Extend (adds multiple elements)
print(numbers.extend([60, 70, 80]))
print(numbers) # [10, 15, 20, 100, 40, 50, 60, 70, 80]


# Removing Elements
numbers = [10, 15, 20, 100, 40, 50, 60, 70, 80]
print(numbers.remove(100)) # Removes first occurrence of 100
print(numbers.pop(2)) # Removes element at index 2
print(numbers.pop()) # Removes last element
del(numbers[1]) # Deletes element at index 1
print(numbers.clear()) # Clears the entire list

