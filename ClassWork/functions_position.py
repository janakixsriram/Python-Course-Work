data = ['xyz@gmail.com','xyz@123']
def login (username,mail,password):
    if mail==data[0] and password==data[1]:
        print(f"{username} - Login Successful")
    else:
        print(f"{username} - Login Fail")
username = input("Enter the username: ")
mail = input("Enter the mail: ")
password = input("Enter the password: ")

login(username,mail,password)
    