# This program prints a hollow diamond star pattern.

n = int(input("Enter an odd number: "))

if n % 2 == 0 or n <= 0:
    print("Please enter a positive odd number.")
else:
    mid = n // 2

    # Upper half
    for i in range(mid + 1):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

    # Lower half
    for i in range(mid - 1, -1, -1):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")

        print()
