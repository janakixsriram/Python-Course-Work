numbers = tuple(map(int,input("Enter numbers:").split()))
x = int(input("Enter number to count:"))
c = numbers.count(x)
print(f"{x} appears {c} times")