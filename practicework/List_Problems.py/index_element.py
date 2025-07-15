items = input("Enter list: ").split()
element = input("Enter element to find: ")

if element in items:
    index = items.index(element)
    print(f"'{element}' found at index: {index}")
else:
    print(f"'{element}' not found in the list.")
