# main.py
import myprograms as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Armstrong Number")
        print("2. Swap Two Numbers")
        print("3. Count Vowels in String")
        print("4. GCD of Two Numbers")
        print("5. Reverse a Number")
        print("6. Sum of Digits")
        print("7. Count Words in Sentence")
        print("8. Convert String to Title Case")
        print("9. Factorial of a Number")
        print("10. Fibonacci Series")
        print("11. Palindrome Check")
        print("12. Find Max in List")
        print("13. Prime Number Check")
        print("14. Remove Duplicates from List")
        print("15. Convert Decimal to Binary")
        print("0. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "1": mp.armstrong_number()
        elif choice == "2": mp.swap_numbers()
        elif choice == "3": mp.count_vowels()
        elif choice == "4": mp.gcd_numbers()
        elif choice == "5": mp.reverse_number()
        elif choice == "6": mp.sum_of_digits()
        elif choice == "7": mp.count_words()
        elif choice == "8": mp.string_title_case()
        elif choice == "9": mp.factorial_number()
        elif choice == "10": mp.fibonacci_series()
        elif choice == "11": mp.palindrome_check()
        elif choice == "12": mp.find_max_list()
        elif choice == "13": mp.prime_check()
        elif choice == "14": mp.remove_duplicates()
        elif choice == "15": mp.decimal_to_binary()
        elif choice == "0":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
