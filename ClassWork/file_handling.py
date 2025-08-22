"""
r- read 
w- write
a- append
r+ read+write
w+ write + read
a+ append+ read

"""
try:
    file = open('for_loop.py','r') ##if try successful else block is executed
except FileNotFoundError: # we can write exception in place of filenotfounderror
    print("File is not present")
else:
    read = file.read()
    file.seek(0)
    readlines = file.readlines()
    file.seek(0)
    readline = file.readline()
    print(f"\nFile content using read() :\n{read}")
    print(f"\nFile content using readlines() :\n{readlines}")
    print(f"\nFile content using readline() :\n{readline}")
    file.close()
finally:
    print("Rest of the code")
    


