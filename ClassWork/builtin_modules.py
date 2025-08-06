import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.sqrt(25))
print(math.pow(2,3))
print(round(12.3))
print(round(12.8))

print(math.ceil(12.3))
print(math.ceil(12.1))
print(math.ceil(12.9))

print(math.floor(12.3))
print(math.floor(12.1))
print(math.floor(12.9))

print(math.fabs(124))
print(math.factorial(6))
print(math.gcd(12,8))
print(math.log(2 , 5))
print(math.sin(90))
print(math.cos(60))
print(math.tan(45))

print(math.degrees(90))
print(math.radians(90))

import random 
print(random.random())
print(random.randint(1,9))
print(random.uniform(1,9))
names = ["amma","nana","chaitra","janaki"]
print(random.choice(names))
print(random.choices(names,k=2))
print(random.shuffle(names),names)

