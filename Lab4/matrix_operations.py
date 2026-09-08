# This program performs different operations on a 3x3 matrix.

matrix = []

print("Enter the elements of 3x3 matrix:")

for i in range(3):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

# Display matrix
print("\nMatrix:")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

# Sum of all elements
total = 0

for i in range(3):
    for j in range(3):
        total += matrix[i][j]

print("\nSum of all elements:", total)

# Sum of main diagonal
diagonal_sum = 0

for i in range(3):
    diagonal_sum += matrix[i][i]

print("Sum of main diagonal:", diagonal_sum)

# Largest and smallest element
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)

# Transpose
print("\nTranspose:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end="\t")
    print()
