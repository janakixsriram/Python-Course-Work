#if we not create dsda file it will automatically creates in write mode

"""
try:
    file = open('dsda.txt','w')
except Exception:
    print("file not present")
finally:
    print("Rest of the code")


try:
    file = open('dsda.txt','w')
except Exception:
    print("file not present")
else:
file.write('Monday we have ecam')
file.close()
"""

##another way to open file

with open('dsda.txt','r+') as file:
    print(file.read())
    file.write('\nFile operations \n')
    file.seek(0)
    print(file.read())
