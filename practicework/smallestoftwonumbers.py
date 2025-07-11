numbers = input("Enter the number sepearated by comma: ")
a, b = map(int, numbers.split(","))
if a<b:
    print(f"{a} is smaller")
else:
    print(f"{b} is smaller")