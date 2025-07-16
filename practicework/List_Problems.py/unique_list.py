numbers = list(map(int,input("Enter list: ").split()))
unique = []
for i in numbers:
    if numbers.count(i) == 1:
        unique.append(i)

print("Unique elements:", unique)