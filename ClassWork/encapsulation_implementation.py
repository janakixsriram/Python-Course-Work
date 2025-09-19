''''
#both are public a and display function
class encap:
    a = 10;
    def display(self):
        print("Welcome")
obj = encap()
print(obj.a)
obj.display()
'''
'''
#private
class encap:
    __a = 10;
    def display(self):
        print("Welcome")
obj = encap()
print(obj.a) #outside the class 
obj.display()
'''
#accesing the inside it work
'''
class encap:
    __a = 10; #private variable
    def display(self): #public
        print("Welcome")
        print(self.__a) #accesing the with in the class  using self 
obj = encap()
obj.display()
'''
class encap:
    __a = 10; #private variable
    def __display(self): #private method
        print("Welcome")
        print(self.__a)
obj = encap()
obj.display()

