date, month, year = input().split("-")
print(f'{year}/{month}/{date}')
 
 
sen = input().split()
for i in sen:
    print(i[::-1],end=' ')

l = list(map(int,input().split()))
while (0 in l):
    l.remove(0)
print(l)

line = input().split()
data = {}
for i in line:
    if i not in data and i!=' ':
        data[i] = line.count(i)
print(data)