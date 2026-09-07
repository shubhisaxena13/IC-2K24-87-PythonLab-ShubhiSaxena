# This program checks whether a number is an Armstrong number
# and prints Armstrong numbers within a given range.


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


number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
elif is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

if start < 0 or end < 0 or start > end:
    print("Invalid range.")
else:
    print("Armstrong numbers in the range:")
    for value in range(start, end + 1):
        if is_armstrong(value):
            print(value, end=" ")
    print()
