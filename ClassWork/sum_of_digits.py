n = int(input("Enter the numbers:"))
sumofdigit = 0
while n>0:
    sumofdigit+=(n%10)
    n = n//10

print(sumofdigit)