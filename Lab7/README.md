#  Python Lab 7 – Time and Space Complexity

##  Aim

To analyze the **time complexity and space complexity** of different Python code snippets using **Big-O notation**, and justify the complexity of each snippet.

---

##  Objectives

* Understand **Time Complexity**.
* Understand **Space Complexity**.
* Analyze loops and nested loops.
* Analyze recursive functions.
* Understand the complexity of searching and sorting-related operations.
* Identify the difference between **linear, quadratic, logarithmic, exponential**, and other complexities.
* Apply **Big-O notation** to Python programs.

---

##  Theory

### Time Complexity

Time complexity represents the amount of time an algorithm takes as the input size increases.

Common time complexities are:

| Complexity   | Name         |
| ------------ | ------------ |
| `O(1)`       | Constant     |
| `O(log n)`   | Logarithmic  |
| `O(n)`       | Linear       |
| `O(n log n)` | Linearithmic |
| `O(n²)`      | Quadratic    |
| `O(n³)`      | Cubic        |
| `O(2ⁿ)`      | Exponential  |

### Space Complexity

Space complexity represents the amount of **extra memory** required by an algorithm as the input size increases.

For recursive functions, the **recursion call stack** is also considered while calculating auxiliary space.

---

#  Snippet 1 – Finding Maximum Element

### Code

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

### Solution

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

**Justification:** The loop examines every element once, so the time grows linearly with `n`, while only a constant number of variables are used.

---

#  Snippet 2 – Checking Duplicates

### Code

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

### Solution

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(1)`

**Justification:** Two nested loops compare pairs of elements, resulting in approximately `n²` comparisons.

---

#  Snippet 3 – Sum of Digits

### Code

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

### Solution

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(log n)`

**Justification:** Each recursive call removes one decimal digit from `n`, so there are approximately `log₁₀(n)` calls.

---

#  Snippet 4 – Printing All Pairs

### Code

```python
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result
```

### Solution

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(n²)`

**Justification:** The two nested loops generate `n²` pairs, and the result list stores all `n²` pairs.

---

#  Snippet 5 – Binary Search

### Code

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

### Solution

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(1)`

**Justification:** Each iteration eliminates approximately half of the remaining search space and only constant extra variables are used.

---

#  Snippet 6 – Matrix Multiplication

### Code

```python
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]

    return result
```

### Solution

**Time Complexity:** `O(n³)`

**Space Complexity:** `O(n²)`

**Justification:** Three nested loops each run approximately `n` times, while the result matrix requires `n²` storage.

---

#  Snippet 7 – Converting Matrix to Sparse Representation

### Code

```python
def to_sparse(matrix):
    triples = []

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))

    return triples
```

### Solution

**Time Complexity:** `O(mn)`

**Space Complexity:** `O(k)`

Where:

* `m` = number of rows
* `n` = number of columns
* `k` = number of non-zero elements

**Justification:** Every matrix element is checked once, giving `mn` operations, while only the `k` non-zero elements are stored.

---

#  Snippet 8 – Nested Processing

### Code

```python
def process(arr):
    n = len(arr)

    for i in range(n):
        print(arr[i])

    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])
```

### Solution

**Time Complexity:** `O(n²)`

**Justification:** The first loop takes `O(n)` and the nested loops take `O(n²)`. Therefore, the dominant term is `O(n²)`.

**Space Complexity:** `O(1)` auxiliary space.

---

#  Snippet 9 – Checking First Ten Values

### Code

```python
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True

    return False
```

### Solution

**Time Complexity:** `O(n)`

**Justification:** The inner loop always runs at most 10 times, which is constant, so `10n` simplifies to `O(n)`.

**Space Complexity:** `O(1)`

---

#  Snippet 10 – Reverse Using a New List

### Code

```python
def reverse_new(arr):
    reversed_arr = []

    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])

    return reversed_arr
```

### Solution

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Justification:** Every element is processed once, while a new list containing all `n` elements is created.

---

#  Snippet 11 – Reverse In-Place

### Code

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
```

### Solution

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

**Justification:** The loop performs approximately `n/2` swaps, which is `O(n)`, and no additional list is created.

---

#  Snippet 12 – Factorial Using Recursion

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
```

### Solution

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Justification:** The function makes one recursive call for each value from `n` down to `1`, creating `n` stack frames.

---

#  Snippet 13 – Recursive Fibonacci

### Code

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Solution

**Time Complexity:** `O(2ⁿ)`

**Space Complexity:** `O(n)`

**Justification:** Each call branches into two recursive calls, producing an exponential number of calls, while the maximum recursion depth is `n`.

---

#  Snippet 14 – Count Pairs With Given Sum

### Code

```python
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0

    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)

    return count
```

### Solution

**Time Complexity:** `O(n)` average case

**Space Complexity:** `O(n)`

**Justification:** The array is traversed once and set lookup/insertion takes `O(1)` average time, while the set can contain up to `n` elements.

---

#  Snippet 15 – Printing All Subsets

### Code

```python
def print_all_subsets(arr):
    n = len(arr)

    for i in range(2 ** n):
        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])

        print(subset)
```

### Solution

**Time Complexity:** `O(n × 2ⁿ)`

**Justification:** There are `2ⁿ` possible subsets, and for each subset the algorithm checks all `n` elements.

**Space Complexity:** `O(n)` auxiliary space for the temporary subset.

---

#  Snippet 16 – Merge Two Sorted Lists

### Code

```python
def merge_sorted(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result
```

### Solution

Let:

* `n` = length of `a`
* `m` = length of `b`

**Time Complexity:** `O(n + m)`

**Space Complexity:** `O(n + m)`

**Justification:** Each element from both lists is processed once and the merged result stores all elements.

---

#  Snippet 17 – Palindrome Check

### Code

```python
def is_palindrome(s):
    return s == s[::-1]
```

### Solution

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Justification:** String slicing creates a reversed copy of the string, requiring `O(n)` time and `O(n)` additional memory.

---

#  Snippet 18 – Flatten a Matrix

### Code

```python
def flatten(matrix):
    flat = []

    for row in matrix:
        for val in row:
            flat.append(val)

    return flat
```

### Solution

Let:

* `m` = number of rows
* `n` = number of columns

**Time Complexity:** `O(mn)`

**Space Complexity:** `O(mn)`

**Justification:** Every matrix element is visited once and all `mn` elements are stored in the new list.

---

#  Snippet 19 – Power Using Recursion

### Code

```python
def power(base, exp):
    if exp == 0:
        return 1

    return base * power(base, exp - 1)
```

### Solution

**Time Complexity:** `O(exp)`
or **`O(n)`** if exponent is represented by `n`.

**Space Complexity:** `O(exp)`

**Justification:** The exponent decreases by one during every recursive call, resulting in `exp` calls and `exp` stack frames.

---

#  Snippet 20 – Fast Power

### Code

```python
def fast_power(base, exp):
    if exp == 0:
        return 1

    half = fast_power(base, exp // 2)

    if exp % 2 == 0:
        return half * half

    return half * half * base
```

### Solution

**Time Complexity:** `O(log exp)`

**Space Complexity:** `O(log exp)`

**Justification:** The exponent is divided by 2 at every recursive call, resulting in logarithmic recursion depth.

---

#  Snippet 21 – Common Element in Two Arrays

### Code

```python
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True

    return False
```

### Solution

Let:

* `n` = size of array `a`
* `m` = size of array `b`

**Time Complexity:** `O(nm)`

**Space Complexity:** `O(1)`

**Justification:** Each element of `a` may be compared with every element of `b`, resulting in `n × m` comparisons.

---

#  Snippet 22 – Frequency Map

### Code

```python
def build_frequency_map(arr):
    freq = {}

    for val in arr:
        freq[val] = freq.get(val, 0) + 1

    return freq
```

### Solution

**Time Complexity:** `O(n)` average case

**Space Complexity:** `O(n)`

**Justification:** The array is traversed once and dictionary operations take `O(1)` average time, while the dictionary can store up to `n` distinct values.

---

#  Complexity Summary

| Snippet                  | Time Complexity | Space Complexity |
| ------------------------ | --------------- | ---------------- |
| 1. Find Maximum          | `O(n)`          | `O(1)`           |
| 2. Duplicate Check       | `O(n²)`         | `O(1)`           |
| 3. Sum of Digits         | `O(log n)`      | `O(log n)`       |
| 4. Print Pairs           | `O(n²)`         | `O(n²)`          |
| 5. Binary Search         | `O(log n)`      | `O(1)`           |
| 6. Matrix Multiplication | `O(n³)`         | `O(n²)`          |
| 7. Sparse Matrix         | `O(mn)`         | `O(k)`           |
| 8. Process               | `O(n²)`         | `O(1)`           |
| 9. First Ten Values      | `O(n)`          | `O(1)`           |
| 10. Reverse New          | `O(n)`          | `O(n)`           |
| 11. Reverse In-Place     | `O(n)`          | `O(1)`           |
| 12. Factorial            | `O(n)`          | `O(n)`           |
| 13. Fibonacci            | `O(2ⁿ)`         | `O(n)`           |
| 14. Pair Sum             | `O(n)` average  | `O(n)`           |
| 15. All Subsets          | `O(n × 2ⁿ)`     | `O(n)`           |
| 16. Merge Sorted         | `O(n + m)`      | `O(n + m)`       |
| 17. Palindrome           | `O(n)`          | `O(n)`           |
| 18. Flatten Matrix       | `O(mn)`         | `O(mn)`          |
| 19. Power                | `O(exp)`        | `O(exp)`         |
| 20. Fast Power           | `O(log exp)`    | `O(log exp)`     |
| 21. Common Element       | `O(nm)`         | `O(1)`           |
| 22. Frequency Map        | `O(n)` average  | `O(n)`           |

---

#  Important Observations

1. A **single loop** over `n` elements generally gives `O(n)`.
2. **Nested loops** over the same input generally give `O(n²)`.
3. Three nested loops generally give `O(n³)`.
4. Binary search has `O(log n)` time because the search space is divided by 2 at every step.
5. Recursive functions may require additional space because of the **call stack**.
6. Creating a new list containing `n` elements requires `O(n)` space.
7. In-place algorithms can reduce auxiliary space to `O(1)`.
8. Generating all subsets requires exponential time because an array of `n` elements has `2ⁿ` possible subsets.
9. Dictionary and set operations are generally `O(1)` on average.
10. When different terms occur together, the **dominant term** is used in Big-O notation.

---

#  Conclusion

This lab helped in understanding how to determine the **time and space complexity** of Python programs.

By analyzing loops, nested loops, recursion, searching, matrix operations, list operations, sets, and dictionaries, we can estimate how efficiently an algorithm uses computational resources.

Big-O notation provides a standard way to describe the growth of an algorithm as the input size increases. Understanding complexity is important for selecting and designing efficient algorithms.

---

##  Topics Covered

* Big-O Notation
* Time Complexity
* Space Complexity
* Linear Complexity
* Quadratic Complexity
* Cubic Complexity
* Logarithmic Complexity
* Exponential Complexity
* Recursion
* Binary Search
* Matrix Operations
* List Operations
* Set and Dictionary Operations
* In-place Algorithms
* Sparse Matrix Representation

---

es of all **22 given Python snippets** were successfully analyzed and justified using Big-O notation.
