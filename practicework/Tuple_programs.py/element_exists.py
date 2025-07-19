elements = tuple(input("Enter items:").split())
check = input("Enter word to check:")
if check in elements:
    print("True")
else:
    print("false")