a=20
b=10
# Arithmetic operators
print("Addition (+) :", a+b) #addition : 30
print("Subtraction (-) :",a-b) #subtraction :10
print("Multiplication (*) :",a*b) #multiplication : 200
print("division (/) :",a/b) #division :2.0
print("Floor division (//) :",a//b) #floor division : 2 
print("Modulus (%) :",a%b) #modulus : 0
print("exponentation (**) :",a**2) #exponentation : 10240000000000

print("\n")
#Comparison Operators
x = 10
y = 5
print("Equal to (==)",x == y) # Output: False
print("Not Equal to (==)",x != y) # Output: True
print("greater than(==)",x > y) # Output: True
print("Less than(==)",x < y) # Output: False
print("Greater than equal to (==)",x >= 10) # Output: True
print("Less than Equal to (==)",y<= 5) # Output: True
print("\\n") # to print \n

# Assignment Operators
x = 10 #Assign
print(x)
x += 5 #Add & Assign
print(x) # x = x + 5 → 15
x *= 2  #Multiply & Assign
print(x) # x = x * 2 → 30
x -= 10 #Subtract & Assign
print(x) # x = x - 10 → 20
print(x) # Output: 20

print("\n")

#Logical Operators (Using Logic Gates)
x = 10
y = 20
print(x > 5 and y < 30) # Output: True (Both conditions are True)
print(x > 15 or y < 30) # Output: True (At least one condition is True)
print(not (x > 5)) # Output: False (Reverses the True condition)

print("\n")

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True

print("\n")

#Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c) # Output: True

print("\n")

#Bitwise Operators (With Binary Representation)
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)
