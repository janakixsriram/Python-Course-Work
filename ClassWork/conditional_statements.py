items = {'shoes','smartwatch','phone','laptop','airpods','toycar'}
print("WELCOME TO AMAZON STORE CENTER".center(50,'*'))
search_input = input("Enter the item:").lower()

if search_input in items:
    print(f"{search_input} found. Buy now!!")
else:
    print(f"{search_input} is out of stock now. we will notify you.")

print("Thankyou")


#  Weekend Budget Plan
amount = int(input("Enter the amount you can spend for weekend: "))
if amount>20000:
    print("Trip to Goa")
elif amount<=15000:
    print("Go for Shopping")
elif amount<=10000:
    print("Clubingg")
elif amount<=5000:
    print("Cafe/Dinner")
elif amount<=2000:
    print("Cinema")
else:
    print("Go And Sleep")


