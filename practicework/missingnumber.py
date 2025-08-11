l = list(map(int,input("Enter numbers: ").split()))
m = []
for i in range(1,100):
    if i not in l:
        m.append(i)
print(m)