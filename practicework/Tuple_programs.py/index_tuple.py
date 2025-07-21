values = tuple(input("Enter values: ").upper())
search_value = input("Enter value to search: ")
# Find indexes
indexes = []
for i in range(len(values)):
    if values[i] == search_value:
        indexes.append(i)

# Output
print("Indexes of", search_value, ":", indexes)