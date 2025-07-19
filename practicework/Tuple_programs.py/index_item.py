items = tuple(input("Enter items:").split())
find = input("Enter item to find:")
i = items.index(find)
print(f"{find} found at index:",i)