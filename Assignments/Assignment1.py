"""Task 1: Take Blinkit Customer Details As Input:
Customer_id : (int)
Customer_name : (str)
Customer_email : (str)
Customer_phone no: (str)
Customer_address : (str)
Customer_area : (str)
Pincode : (int)
Customer_segment : (str)
total_orders : (int)
avg_order_value : (float)


Task 2: Display Customer Details Using Different Formatting Methods
After collecting the input
print the product details using:
 Comma Separation (sep=',') Percentage Formatting (% operator)
 f-strings (f"")
 .format() method

Example User Input:
    
Enter Customer_id : 97475543
Enter Customer_name : Niharika Nagi
Enter Customer_email : ektataneja@gmail.com
Enter Customer_phone no : 912987579691
Enter Customer_address : 23,Nayar Path, Bihar Sharif-154625
Enter Customer_area : Udupi
Enter Pincode : 321865
Enter Customer_segment : Premium
Enter total_orders : 13
Enter avg_order_value : 451.92"""






Customer_id = int(input("Enter Customer_id :"))
Customer_name = input("Enter Customer_name :")
Customer_email = input("Enter Customer_email :")
Customer_phone_no = int(input("Enter Customer_phone_no :"))
Customer_address = input("Enter Customer_address: ")
Customer_area = input("Enter Customer_area: ")
pincode = input("Enter Pincode: ")
Customer_segment = input("Enter Customer_segment: ")
total_orders = int(input("Enter total_orders: "))
avg_order_value = float(input("Enter avg_order_value: "))

print()

print("USING STAR SEPERATOR")
print("Customer_id: 97475543", "Customer_name: Niharika Nagi", "Customer_email: ektataneja@gmail.com" ,sep="*"  )

print()

print("USING PERCENTAGE FORMATTING(% OPERATOR)")
print("pincode: %s | total_orders: %d" %(pincode,total_orders))

print()

print("USING F-STRINGS(f"" )")
print(f"Customer_Segment: {Customer_segment}|average_order_value: {avg_order_value}")

print()

print("USING.format() METHOD")
print("Customer_phone_no: {} | Customer_Address : {}".format(Customer_phone_no,Customer_address))

print()