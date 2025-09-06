"""
class student:
    name = "janaki"
    rno = 1234 
    branch = "cse"
    def read(self):
        print("Reading")
#object_name = class_name
abc = student()
print("name=",student.name)
print("roll number=",student.rno)
print("branch=",student.branch)
abc.read()   
"""

"""     
#addding local variables in function rollno
class student:
    name = "janaki"
    rno = 1234 
    branch = "cse"
    def read(self):
        rollno = 234
        print("Roll number=",rollno)
        print("Reading")
#object_name = class_name
abc = student()
print("name=",student.name)
print("roll number=",student.rno)
print("branch=",student.branch)
abc.read()  

"""
"""
#what if we have same variable in instance and inside def function local variables

class student:
    name = "janaki"
    rno = 1234 
    branch = "cse"
    def read(self):
        rno = 231
        print("r.no=",rno)
        print("Reading")
#object_name = class_name
abc = student()
print("name=",student.name)
print("roll number=",student.rno)
print("branch=",student.branch)
abc.read()  

"""

#how to access instance variable which are inside the class in function
#to access we use self 

class student:
    name = "janaki"
    rno = 1234 
    branch = "cse"
    def read(self):
        print("instance variable name=",self.name)
        print("Reading")
#object_name = class_name
abc = student()
print("name=",student.name)
print("roll number=",student.rno)
print("branch=",student.branch)
abc.read()   
