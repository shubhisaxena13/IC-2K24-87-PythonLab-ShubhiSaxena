# This program checks whether a number is a perfect number
# and prints all perfect numbers up to a given limit.


def is_perfect(number):
    if number <= 0:
        return False

    total = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor

    return total == number


number = int(input("Enter a number: "))

if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")

limit = int(input("Enter the limit: "))

if limit <= 0:
    print("Please enter a positive limit.")
else:
    print("Perfect numbers up to", limit, ":")
    for value in range(1, limit + 1):
        if is_perfect(value):
            print(value, end=" ")
    print()
