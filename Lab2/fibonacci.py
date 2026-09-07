# This program prints the Fibonacci series using a loop and recursion
# and counts the number of recursive function calls.

recursive_calls = 0


def fibonacci_loop(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


def fibonacci_recursive(n):
    global recursive_calls

    recursive_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter number of terms: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci using loop:")
    fibonacci_loop(n)

    recursive_calls = 0

    print("Fibonacci using recursion:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print()
    print("Recursive function calls:", recursive_calls)
