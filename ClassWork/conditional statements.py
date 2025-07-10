items = {'shoes','smartwatch','phone','laptop','airpods','toycar'}
print("WELCOME TO AMAZON STORE CENTER".center(50,'*'))
search_input = input("Enter the item:"),lower()

if search_input in items:
    print(f"{search_input} found. Buy now!!")
else:
    print(f"{search_input} is out of stock now. we will notify you.")
    
