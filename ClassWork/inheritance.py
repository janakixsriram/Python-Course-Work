#single inheritance
# parent class not need to access from child class we can inherit the properties of parent class


"""
class A: #parent clss
    def display_a(self):
        print("Parent Class A")
class B: #child class
    def display_b(self):
        print("child class B<-A")
a = A() # calling 
a.display_a()


b = B()
b.display_b()
b.display_a() # accessing child class from parent class


"""

# Multiple inheritance
# multiple parents class with single child class
"""
class A: #parent clss
    def display_a(self):
        print("Parent Class A")
class B: #child class
    def display_b(self):
        print("Parent class B")
class C: 
    def display_c(self):
        print("Parent Class C")
class D(A,B,C): 
    def display_d(self):
        print("Child Class A,B,C->")

d = D()
d.display_a()
d.display_b()
d.display_c()
d.display_d()

"""

#Multi-level inheritance

class A: #parent Class
    def display_a(self):
        print("Parent Class A")
class B(A): # A is the parent class for B which can inherit the properties of A 
    def display_b(self):
        print("Parent class B")
class C(B): #B is the parent class for A which can inherit the properties of B and A
    def display_c(self):
        print("Parent Class C")
class D(C): 
    def display_d(self):
        print("Child Class A,B,C->")

d = D()
d.display_a()
d.display_b()
d.display_c()
d.display_d()

# heirachical single parent multiple childs

class A: #parent Class
    def display_a(self):
        print("Parent Class A")
class B(A): 
    def display_b(self):
        print("Parent class B")
class C(A): 
    def display_c(self):
        print("Parent Class C")
class D(A): 
    def display_d(self):
        print("Child Class A,B,C->")

b = B()
b.display_a()
b.display_b()

c = C()
c.display_a()
c.display_c()


d = D()
d.display_a()
d.display_d()

# Example whatsaap

class Status2015:
    def View(self):
        print("you can view status")
    def reply(self):
        print("You can reply")
    def Caption(self):
        print("you can caption")

print('\njanaki')
janaki = Status2015()
janaki.View()
janaki.reply()
janaki.Caption()
    

class Status2020:
    def uploadImg(self):
        print("you can upload Img")
    def uploadVid(self):
        print("You can upload video")
    def privacy(self):
        print("You can add privacy")



print('\nsriram')
sriram = Status2020()
sriram.uploadImg()
sriram.uploadVid()
sriram.privacy()



"""
class Status2015:
    def view(self):
        print("You can view status")
    def reply(self):
        print("You can reply")
    def caption(self):
        print("You can add caption")

class Status2020(Status2015):
    def uploadImg(self):
        print("You can upload Image")
    def uploadVid(self):
        print("You can upload video -30 sec")
    def privacy(self):
        print("You can select who can see your status")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy")
    def reaction(self):
        print("You can send reactions")           
    def like(self):
        print("You can like the status")


class Status2024(Status2020):
    def statusrings(self):
        print("Color is added to the status display")
    def mute(self):
        print("You can mute the other's status")
    def filters(self):
        print("You can filters")

    
class Status2025(Status2023,Status2024):
    def music(self):
        print("You can add music")
    def mention(self):
        print("You can mention them")
    def collab(self):
        print("You can share your status from insta or fb")
    def voicenote(self):
        print("You can voice note")


print("\nSheshu")       
sheshu= Status2015()
sheshu.view()
sheshu.reply()
sheshu.caption()

print("\nHemanth")
hemanth=Status2020()
hemanth.uploadImg()
hemanth.uploadVid()
hemanth.privacy()
hemanth.view()
hemanth.reply()
hemanth.caption()

print("\nRasool")
rasool=Status2023()
rasool.uploadImg()
rasool.uploadVid()
rasool.privacy()
rasool.view()
rasool.reply()
rasool.caption()
rasool.ProfilePrivacy()
rasool.reaction()
rasool.like()

print("\nTarit")
tarit=Status2024()
tarit.uploadImg()
tarit.uploadVid()
tarit.privacy()
tarit.view()
tarit.reply()
tarit.caption()
tarit.statusrings()
tarit.mute()
tarit.filters()


print('\nVarun')
varun=Status2025()
varun.uploadImg()
varun.uploadVid()
varun.privacy()
varun.view()
varun.reply()
varun.caption()
varun.statusrings()
varun.mute()
varun.filters()
varun.ProfilePrivacy()
varun.reaction()
varun.like()
"""
