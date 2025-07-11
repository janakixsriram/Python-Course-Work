numbers = (input("Enter the values seperated by comma: "))
a, b = map(int, numbers.split(","))
if a>b:
    print(f"{a} is greater")
elif b>a:
    print(f"{b} is greater")
else:
    print("Both numbers are equal")
