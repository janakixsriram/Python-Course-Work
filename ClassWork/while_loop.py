bullets = 10
while bullets>0:
    bullets-=1
    print(f"shoot(),{bullets} are left")


print()
"""while with if else"""

bullets = 10
while bullets > 0:
    if bullets<13:
        print("user dead, Game over")
        break
    bullets-=1
    print(f"shoot {bullets} are left")
else:
    print("Game over!! You win")


print()

email,pwd = 'xyz@gmail.com','xyz@123'
max_attempts=5

while max_attempts>0:
    useremail = input("Enter the email: ")
    password = input("Enter the password: ")
    if useremail==email and pwd == password:
        print("Login Successful")
        break
    else:
        print("Invalid Login")
    max_attempts-=1
else:
    print("Try after some time!!")