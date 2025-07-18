str1 = 'Hello'
str2 = "World"
str3 = '''This is a multi-line
string example.'''
print(str1)
print(str2)
print(str3)

#Operations on Strings
#Concatenation (+) - Joining two or more strings.
#Repetition (*) - Repeating a string multiple times.
#Indexing - Accessing individual characters using indices.
#Slicing - Extracting a part (substring) of the string.
#Membership (in, not in) - Checking if a substring exists within a string.

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World
# Repetition
print("Python! " * 3) # Output: Python! Python! Python!
# Indexing
text = "Python"
print(text[0]) # Output: P (1st character)
print(text[-1]) # Output: n (last character)
# Slicing
print(text[0:3]) # Output: Pyt (from index 0 to 2)
print(text[:4]) # Output: Pyth (default start is 0)
print(text[2:]) # Output: thon (from index 2 to end)
# Membership
print('Pyt' in text) # Output: True
print('Java' not in text) # Output: True



#Built-in String Functions

# 1. len()
text = "Hello World"
print(len(text)) # Output: 11
# 2. max() and min()
print(max("abcXYZ")) # Output: 'c' (highest ASCII value)
print(min("abcXYZ")) # Output: 'X' (lowest ASCII value)
# 3. sorted()
print(sorted("python")) # Output: ['h', 'n', 'o', 'p', 't','y']
# 4. chr() and ord()
print(ord('A')) # Output: 65 (ASCII value of 'A')
print(chr(97)) # Output: 'a' (character for ASCII value 97)

#Complete List of Python String Methods with Examples
# 1. Case Conversion Methods

name = 'janaki'
print(name.upper()) #upper()
print(name.lower()) #lower()
print(name.capitalize()) #capitalize()
print(name.title()) #title
print(name.swapcase()) #swapcase()

# 2.Alignment & Formatting Methods
person = "chaitra"
print(person.center(20,'*')) #center(width,fillchar)
print(person.ljust(10, "-")) #ljust(width,fillchar)
print(person.rjust(15,"&"))  #rjust(width,fillchar)
print(person.zfill(10))  #zfill(width)

# 3.Search & Find Methods
item = '''Banana'''
print(item.find('n')) #find(sub)
print(item.rfind('n'))
print(item.index("a"))
print(item.rindex("a"))
print(item.count("a"))

# 4. String Testing Methods (Boolean Results)
word = 'python programming language'
print(word.startswith("py"))
print(word.endswith("age"))
print(word.isalpha())
print(word.isalnum())
print(word.islower())
print(word.isupper())
print(word.isspace())
print(word.istitle())
print(word.isidentifier())

#5.Replace & Modify Methods
key = "ramu"
print(key.replace('a','o'))
print(key.translate(str.maketrans("a" , "x")))


#6. Splitting & Joining Methods
string = "sriram,janaki,hari"
print(string.split("*"))
print(string.rsplit("%"))
print(" ".join(["Hello", "World"]))
print(string.partition("-"))
print(string.rpartition("-"))

#7. Whitespace & Trimming Methods
town = 'Kanigiri'
print(town.strip())
print(town.lstrip())
print(town.rstrip())











