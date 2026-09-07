# This program is a menu-driven application that combines
# Armstrong, Prime, Perfect, Palindrome, Fibonacci and Pattern programs.


def is_armstrong(number):
    if number < 0:
        return False

    digits = len(str(number))
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == number


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def is_perfect(number):
    if number <= 0:
        return False

    total = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor

    return total == number


def is_palindrome(number):
    if number < 0:
        return False

    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    return original == reverse


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


def patterns(rows):
    print("\nRight-angled triangle")

    for i in range(1, rows + 1):
        print("* " * i)

    print("\nNumber pattern")

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nCentered pyramid")

    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * (2 * i - 1))


while True:

    print("\n----- PYTHON LAB MENU -----")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        number = int(input("Enter a number: "))

        if is_armstrong(number):
            print(number, "is an Armstrong number.")
        else:
            print(number, "is not an Armstrong number.")

    elif choice == "2":

        number = int(input("Enter a number: "))

        if is_prime(number):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")

    elif choice == "3":

        number = int(input("Enter a number: "))

        if is_perfect(number):
            print(number, "is a perfect number.")
        else:
            print(number, "is not a perfect number.")

    elif choice == "4":

        number = int(input("Enter a number: "))

        if is_palindrome(number):
            print(number, "is a palindrome.")
        else:
            print(number, "is not a palindrome.")

    elif choice == "5":

        n = int(input("Enter number of terms: "))

        if n < 0:
            print("Please enter a non-negative number.")
        else:
            fibonacci(n)

    elif choice == "6":

        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Please enter a positive number.")
        else:
            patterns(rows)

    elif choice == "7":

        print("Exiting program...")
        break

    else:

        print("Invalid choice. Please try again.")
