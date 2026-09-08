# This program prints a right-angled star pattern.

n = int(input("Enter number of rows: "))

if n > 0:
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
else:
    print("Please enter a positive number.")
