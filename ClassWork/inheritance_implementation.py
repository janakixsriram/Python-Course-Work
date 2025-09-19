"""
#single inheritance
class parent:
    def display(self):
        print("Parent Class")
class child(parent):
    def show(self):
        print("Child Class")

#creating the object
#obj_name = class_name

c = child()
c.display()
c.show()
"""
"""
#Multi-level Inheritance:

class grandparent:
    def display(self):
        print("Grand Parent Class")
class parent(grandparent):
    def show(self):
        print("Parent class")
class child(parent):
    def cdisplay(parent):
        print("Child Class")

c = child()
c.display()
c.show()
c.cdisplay()
"""
"""
#Hierachical Inheritance

class parent:
    def display(self):
        print("PARENT CLASS")
class child1(parent):
    def c1display(self):
        print("CHILD1 CLASS")
class child2(parent):
    def c2display(self):
        print("CHILD2 CLASS")

c1 = child1()
c1.display()
c1.c1display()

c2 = child2()
c2.display()
c2.c2display()
"""

#multiple-inheritance

class father:
    def fdisplay(self):
        print("FATHER CLASS")
class mother:
    def mdisplay(self):
        print("MOTHER CLASS")
class child(father,mother):
    def cdisplay(self):
        print("CHILD")
c = child()
c.fdisplay()
c.mdisplay()
c.cdisplay()