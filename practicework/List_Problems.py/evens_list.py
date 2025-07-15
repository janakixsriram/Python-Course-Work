num = []
numbers = list(map(int,input("Enter numbers: ").split()))
for i in numbers:
    if (i %2 == 0):
        num.append(i)
print(num)