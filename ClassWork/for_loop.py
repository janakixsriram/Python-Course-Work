num = int(input("Enter the table number : "))
for i  in range(1,21):
    print(f"{i}. {num} * {i} = {num*i} ")

name = "janaki sriram"
for i in name:
    print(i)

number = int(input("Enter a number:"))
for i in range(1,number):
    print(i)

s = "venkateswarlu bagyalakshmi Chaitra janaki sriram".lower()
n = len(s)
print(n)
ch = input("Enter the char: ").lower()

for i in range(n):
    if s[i] == ch:
        print(ch,i)

n = "janaki"
l = len(n)
print(l)
for i in range(l):
    print(i)


products = ['cycle','watch','laptop','mobile','mouse']
items=input("Enter the items: ").split()

for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not available")
