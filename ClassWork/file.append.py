"""
try:
    file = open('dsda.txt','a+')
except Exception:
    print("file not present")
else:
    file.write('monday we have exam \n')

finally:
    print("Rest of the code")
"""

file = open('janaki.txt','a')
lines=["sriram segu","chaitra segu"]
file.writelines(lines)
file.close()