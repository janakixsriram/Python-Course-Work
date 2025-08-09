f = int(input("Enter a number:"))
fact = 1
if f == 0 or f == 1:
    print("1")
else:
    for i in range(1,f+1):
        fact *= i
print(fact)
