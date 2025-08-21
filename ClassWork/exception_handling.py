NameError
IndexError
KeyError
ValueError

"""
try:
    a = 10
    k = k+10
except IndexError:
    print("Index error")

"""
"""
try:
    a = 10
    k = k+10
except NameError:
    print("K is not defined") # Then it will not raise error with the use except block

try:
    a= 10
    a = a+10
    l = [1,3,4]
    k = l[2]
    d ={1:2,2:4,3:9}
    print(d[2])
    b = int(input("Enter a number: "))
    print(b)
    c = 1 + "1"
except NameError:
    print("a is not defined")
except IndexError:
    print("You Have entered the out of range value")
except KeyError:
    print("Key is not present")
except TypeError:
    print("You can't add 2 diff types")

## single line code 
except (NameError,IndexError,KeyError,TypeError) as e:
    print(f"Error occured: {e}")
#single line code
except Exception as e:
    print(f"Error occured on: {e}")

"""
"""
try:
    a= 10
    a = a+10
    l = [1,3,4]
    k = l[2]
    d ={1:2,2:4,3:9}
    print(d[2])
    b = int(input("Enter a number: "))
    print(b)
    c = 1 + 12
except Exception as e: #except is keyword e exception is what is error willfind 
    print(f"Error occured on: {e}")
else:
    print("No errors")
    print(c)
"""
"""
#using finally
try:
    a= 10
    a = a+10
    l = [1,3,4]
    k = l[2]
    d ={1:2,2:4,3:9}
    print(d[2])
    b = int(input("Enter a number: "))
    print(b)
    c = 1 + 12
except Exception as e:
    print(f"Error occured on: {e}")
else:
    print("No errors")
    print(c)
finally: #if you have or haven't have errors in try block the finnally block executes by default
    print("Code exceuted")
"""
"""
try:
    amount = int(input("Enter the amount: "))
except exception as e:
    print(f"Error occured: {e}")
else:
    print("No errors")
    print("You can withdraw")
finally:
    print("------Remove your card------")

"""
# if we enter amount as -4234 it will not raise error to overcome we use raise 
try:
    amount = int(input("Enter the amount: "))
    if amount < 0:
        raise Exception("Enter the positive value")
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No errors")
    print("You can withdraw")
finally:
    print("------Remove your card------")
