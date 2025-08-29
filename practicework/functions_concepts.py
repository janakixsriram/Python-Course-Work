#Required Arguments:
def required(name,age):
    print("Name:",name)
    print("Age:",age)
    print("\n")
required("JanakiSriram Segu", 22)

#Keyword arguments:
def keyword(dateofbirth,place,hobbies,language):
    print("DateofBirth:",dateofbirth)
    print("Place:",place)
    print("Hobbies:",hobbies)
    print("Language:",language)
    print("\n")
keyword(place = "Markapur",dateofbirth = 19-9-2003,language = "Telugu",hobbies = "Typing")

#default arguments:
def default(name,location = 'kanigiri'):
    print("Name:",name)
    print("Location:",location)
    print("\n")
default(name = "sriram",location = "Hyderabad")
default(name = "AmmaNannaChaitra")

#variable length arguments:
def variablelength (*coachingcenter):
    for i in coachingcenter:
        print(i)
variablelength("codegnan","qspiders","jspiders","360digitmg")

#keyword length arguments:
def kwags(**information):
    print("DateOfBirth:",information["dateofyear"])
    print("Course:",information["Course"])
    print("Intrest:",information["Intrest"])
kwags(dateofyear = 2003,Course = "Data Analytics",Intrest = "Typing")
    
def data(**stu):
    print("Student Name:", stu["Student"])
    print("Student Section:",stu["Section"])
data(Student = "Jack",Section = "kt")


#Using looping key value pairs
def data(**stu):
    print("𝐔𝐬𝐢𝐧𝐠 𝐋𝐨𝐨𝐩𝐢𝐧𝐠:")
    for key,value in stu.items():
        print(f"{key}: {value}")
data(Student = "Jack",Section = "kt")



"""
#Better Version (looping all key-value pairs):
def kwags(**information):
    for key, value in information.items():
        print(f"{key}: {value}")

kwags(dateofyear=2003, Course="Data Analytics", Intrest="Typing")
"""