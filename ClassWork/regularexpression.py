import re
"""
#match()
# like starts with
res = re.match('hello','hello world') #no need of r because it is only test when we use combination of []{} is needed r
print(res.group() if res else "No pattern")
"""
"""
res = re.match(r'[a-z]' 'hello world')  # r-> raw expression which includes {},[]
print(res.group() if res else "No Pattern")
"""

"""
#search()
res = re.match(r'[0-9] {2}','ds-da-14-15') #{2} #is for length only two digits is needed
print(res.group() if res else "No pattern")
"""
"""
#findall()

res = re.findall(r'[0-9]{2}','PFS-30 & PFS-31 & PFS-32 & DSDS-12-14') #{2} finding all the pattern exists in res which e digit
print(res)
"""

"""
#finditer() position it will result when it occurs
res = re.finditer(r'[0-9]{2}','PFS-3056165 & PFS-31365456  & DSDS-12-14') 

for i in res:
    print(i.group(),i.start())
"""
#fullmatch

#res = re.fullmatch(r'(aeiou)','aeiou') 
#res = re.fullmatch(r'(aeiou) *','aeouu') 
#res = re.fullmatch(r'\d{10}', '9959194107') 
#res = re.fullmatch(r'^[6-9]\d{9}', '5659194107') # starts from 6-9 is valid
#res = re.fullmatch(r'DA-..', 'DA-14') 

#res = re.fullmatch(r'(aeiou)+','aeiouaeiou') #+ is for multiple allow
#print(res.group() if res else "No pattern")


#findall()
#res = re.findall(r'D..', 'Dad Dog Dear') 
# res = re.findall(r'\w','python pythonx psthon psxhin' )#\s\S\W
#res = re.findall(r'\S','python pythonx psthon psxhin' )#\s\S\W space 
#res = re.findall(r'\W','python pythonx psthon psxhin' )#\s\S\W

#print(res)

#split()
#res = re.split(r'[,;"-"]','python,pythonx;psthon"psxhin-python pthon' ) # split by symbols 
#print(res)

#sub # replace

#res = re.sub(r'[aeiouAEIOU]','*',' python Programming Language') # replacing with star symbol when aeiouAEIOU encounters in string
#print(res)


#res = re.search(r'[a-z] * [0-9]$', 'python Programming Language32') ->$ is for endswith
#print("yes")


#res = re.search(r'h?i' 'hi','hei') ->? matches 0 or 1 occurence
#print("yes")

res = re.findall(r'\b\d{2}\b','34 32 64 57 2324 5754 76 54 23 4345 6735 8666 45') 
print(res)