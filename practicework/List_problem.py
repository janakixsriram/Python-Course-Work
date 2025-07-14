numbers = []#empty list to store m=numbers
n = int(input("Enter how many numbers : "))
for i in range(1, n+1):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
print("The list is:",numbers)

