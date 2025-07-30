n = int(input("Enter the numbers:"))
l = []
for i in range(1, n+1):
    if i%2==0:
        l.append(i)
print(l)

"""
k = [i for i in range(1, n+1) if i%2==0]

print(k)
"""

d = []
for i in range(5):
    d.append(i*i)
print(d)


"""
for(i*i for i in range(5))
"""
s = 'python'
l= []
for i in s:
    s.append(i.upper())
print(s)

s = [i.upper() for i in s]

j = 'python'
v = 'aeiouAEIOU'
o = []
for i in j:
    for i in v:
        o.append(i)
print(o)

"""
o = [i for i in j if i in v]
"""

s = 'python programming language'

l =[]
for i in s:
    if i.islower():
        l.append(i)
print(i)

l = [i for i in s if i.islower()]

s = '1234dfhgk6789'
l = []
for i in s:
    if i.isdigit():
        l.append(i)
    else:
        l.append(0)

'''l = [i for i in s if i.isdigit() else 0]'''

'''
for set comprehsion use{ }
    
for dictionary comprehension

l = {key:val for key in seq } dictionary comprension
l = [val for val in seq] list comprension
l = {val for val in seq}  sets comprension
'''


names = {'janaki','sriram','chaitra'}
d = {i:'Absent' for i in names}
print(d)


k = {1:1, 2:4 , 3:9, 4:16}

d = {i:i*i for i in range(1,5)}



s = 'python'
l = [i.upper() for i in s]
print(l)
""" converting output as list to string print("".join(l)) """ 