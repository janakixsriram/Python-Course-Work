f = input("Enter String: ")
c = input("Character to count: ")
count = 0
for i in f:
    if c in i:
        count+= 1
print(count)



'''
f = input("Enter String: ")
c = input("Character to count: ")
count = []
for i in f:
    if c == i:
        count.append(i)
print("count",len(count))
'''
