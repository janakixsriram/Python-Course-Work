year = int(input("Enter a Year to check Leap year or not: "))
if (year %  100 == 0) and (year % 400 == 0):
    print(f"{year} is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")