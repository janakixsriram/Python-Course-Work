list1 = list(map(int,input("Enter first List:").split()))
list2 = list(map(int,input("Enter second List:").split()))
common = list(set(list1) & set(list2))
print("common elements:",common)
