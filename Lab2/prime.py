# This program checks whether a number is prime
# and prints all prime numbers up to a given limit.


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

limit = int(input("Enter the limit: "))

if limit < 2:
    print("There are no prime numbers up to", limit)
else:
    print("Prime numbers up to", limit, ":")
    for value in range(2, limit + 1):
        if is_prime(value):
            print(value, end=" ")
    print()
