#reverse a string using functions
"""
def reverse(name):
    return name[::-1]
name = input("Enter name to reverse: ")
result = reverse(name)
print(result)

"""
"""

def cv(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for i in s:
        if i in vowels:
            count+= 1
    if count == 0:
        return "No Vowels Exists in String"
    else:
        return count
s = input("Enter a string: ")
res = cv(s)
print(res)
"""
"""
#maximum of 3 numbers
def max3(a,b,c):
    return max(a,b,c)
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
res = max3(a,b,c)
print(res)
"""
"""
#area of circle using functions
def ac(r,p=3.14):
    return p*r**2
r = int(input("Enter radius: "))
res = ac(r)
print(res)
"""
#function calculate simple intrest

def si(P,R,T):
    return (P*R*T) /100
P = int(input("Enter Pincipal Amount: "))
R = int(input("Enter Rate of intrest: "))
T = int(input("Enter Time: "))
res = si(P,R,T)
print(res)

