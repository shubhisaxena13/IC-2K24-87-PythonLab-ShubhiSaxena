# This program checks whether a number and a string are palindromes.


def number_palindrome(number):
    if number < 0:
        return False

    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    return original == reverse


def string_palindrome(text):
    return text == text[::-1]


number = int(input("Enter a number: "))

if number_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")


text = input("Enter a string: ")

if string_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
