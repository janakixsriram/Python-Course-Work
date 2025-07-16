numbers = list(map(int,input("Enter numbers: ").split()))
c = 0
for i in numbers:
    if i %2 == 0:
        c = c + i
print("Sum of even numbers: ",c)