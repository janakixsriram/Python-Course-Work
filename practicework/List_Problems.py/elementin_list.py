list = input("Enter list:").split()
c = input("Enter an element to check:")

if c in list:
    print(f"Does list contain '{c}'? yes")
else:
    print(f"Does list contain '{c}'? No")