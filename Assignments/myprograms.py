# my_programs.py

def armstrong_number():
    print("🧠 Program: Armstrong Number\n")
    print("""
def is_armstrong(num):
    s = str(num)
    power = len(s)
    return num == sum(int(d)**power for d in s)
""")
    print("🧪 Test Case 1: is_armstrong(153) -> True")
    print("🧪 Test Case 2: is_armstrong(123) -> False")
    print("📝 Explanation: Armstrong number is equal to the sum of its digits raised to the power of number of digits.\n")


def swap_numbers():
    print("🧠 Program: Swap Two Numbers\n")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print("🧪 Test Case 1: swap(10, 20) -> (20, 10)")
    print("🧪 Test Case 2: swap(5, -1) -> (-1, 5)")
    print("📝 Explanation: Uses tuple unpacking to swap values without a temporary variable.\n")


def count_vowels():
    print("🧠 Program: Count Vowels in String\n")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
""")
    print("🧪 Test Case 1: count_vowels('hello') -> 2")
    print("🧪 Test Case 2: count_vowels('sky') -> 0")
    print("📝 Explanation: Iterates through string and counts vowels.\n")


def gcd_numbers():
    print("🧠 Program: GCD of Two Numbers\n")
    print("""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""")
    print("🧪 Test Case 1: gcd(48, 18) -> 6")
    print("🧪 Test Case 2: gcd(7, 13) -> 1")
    print("📝 Explanation: Uses Euclidean algorithm to compute greatest common divisor.\n")


def reverse_number():
    print("🧠 Program: Reverse a Number\n")
    print("""
def reverse_num(n):
    return int(str(n)[::-1])
""")
    print("🧪 Test Case 1: reverse_num(1234) -> 4321")
    print("🧪 Test Case 2: reverse_num(900) -> 9")
    print("📝 Explanation: Converts number to string, reverses it, then back to integer.\n")


def sum_of_digits():
    print("🧠 Program: Sum of Digits\n")
    print("""
def sum_digits(n):
    return sum(int(d) for d in str(n))
""")
    print("🧪 Test Case 1: sum_digits(1234) -> 10")
    print("🧪 Test Case 2: sum_digits(99) -> 18")
    print("📝 Explanation: Converts number to string, iterates digits, and sums them.\n")


def count_words():
    print("🧠 Program: Count Words in Sentence\n")
    print("""
def count_words(sentence):
    return len(sentence.split())
""")
    print("🧪 Test Case 1: count_words('Hello world!') -> 2")
    print("🧪 Test Case 2: count_words('Python is great') -> 3")
    print("📝 Explanation: Splits sentence by spaces and counts words.\n")


def string_title_case():
    print("🧠 Program: Convert String to Title Case\n")
    print("""
def to_title_case(s):
    return s.title()
""")
    print("🧪 Test Case 1: to_title_case('hello world') -> 'Hello World'")
    print("🧪 Test Case 2: to_title_case('python programming') -> 'Python Programming'")
    print("📝 Explanation: Uses built-in title() function.\n")


def factorial_number():
    print("🧠 Program: Factorial of a Number\n")
    print("""
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
""")
    print("🧪 Test Case 1: factorial(5) -> 120")
    print("🧪 Test Case 2: factorial(0) -> 1")
    print("📝 Explanation: Uses recursion to compute factorial.\n")


def fibonacci_series():
    print("🧠 Program: Fibonacci Series\n")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
""")
    print("🧪 Test Case 1: fibonacci(5) -> [0,1,1,2,3]")
    print("🧪 Test Case 2: fibonacci(7) -> [0,1,1,2,3,5,8]")
    print("📝 Explanation: Iteratively adds last two numbers to generate sequence.\n")


def palindrome_check():
    print("🧠 Program: Check Palindrome\n")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print("🧪 Test Case 1: is_palindrome('madam') -> True")
    print("🧪 Test Case 2: is_palindrome('hello') -> False")
    print("📝 Explanation: Compares string with its reverse.\n")


def find_max_list():
    print("🧠 Program: Find Maximum in List\n")
    print("""
def max_in_list(lst):
    return max(lst)
""")
    print("🧪 Test Case 1: max_in_list([1,2,3,4]) -> 4")
    print("🧪 Test Case 2: max_in_list([-5,0,9]) -> 9")
    print("📝 Explanation: Uses Python’s built-in max() function.\n")


def prime_check():
    print("🧠 Program: Check Prime Number\n")
