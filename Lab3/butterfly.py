# This program prints a butterfly star pattern.

n = int(input("Enter number of rows: "))

# Upper half
for i in range(1, n + 1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)

# Lower half
for i in range(n - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)
