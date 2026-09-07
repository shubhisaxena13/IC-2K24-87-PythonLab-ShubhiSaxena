# This program prints three different patterns using nested loops.

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Please enter a positive number.")

else:
    print("\n1. Right-angled triangle")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("\n2. Number pattern")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\n3. Centered pyramid")

    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()
