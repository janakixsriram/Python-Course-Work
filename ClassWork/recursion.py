n = int(input())
for i in range(1,n+1):
    print(i) 

def update(n):
    if n == 0:
        return
    print("Before:",n)
    update(n-1)
    print("After:",n)

n = int(input())
update(n)