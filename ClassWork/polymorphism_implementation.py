"""
a = "janaki"
b = "sriram"
print(a+b)

a = 23
b = 12
print(a+b)
"""

class moverload:
    def display(self,a=None,b=None):
        print(a,b)

obj = moverload()
obj.display()
obj.display(10)
obj.display(34,22)

        