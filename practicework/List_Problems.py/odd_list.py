num = []
numbers = list(map(int,input("Enter the numbers : ").split()))
for i in numbers:
    if(i %2 == 1):
        num.append(i)
print("The odd numbers are: ",num)
