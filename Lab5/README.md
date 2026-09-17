# Python Lab 5

## Menu-Driven Programs and Guessing Games

### Objective

The objective of this lab is to implement Python programs using functions, loops, conditional statements, menu-driven programming, input validation, random number generation, and binary-search style logic.

---

## Programs Included

1. ATM Simulation
2. Student Grade Calculator
3. Reverse Guessing Game
4. Guessing Game with Hints and Scoring
5. Combined Application

---

# 1. ATM Simulation

### Aim

To develop a menu-driven ATM simulation that allows the user to check balance, deposit money, withdraw money, change the PIN, and exit the program.

### Logic

The program starts with a fixed balance and PIN. The user must enter the correct PIN before accessing the ATM menu. The program repeatedly displays the menu and performs the selected operation. Before withdrawing money, the program checks whether the withdrawal amount is within the available balance. If the amount is greater than the balance, the transaction is rejected.

### Sample Input

```text
Enter your PIN: 1234
Enter your choice: 1
Enter your choice: 2
Enter deposit amount: 1000
Enter your choice: 3
Enter withdrawal amount: 7000
Enter your choice: 5
```

### Sample Output

```text
----- ATM MENU -----
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit

Current Balance: ₹ 5000

Amount deposited successfully.
New Balance: ₹ 6000

Transaction rejected: Insufficient balance.

Thank you for using the ATM.
```

### Invalid Input / Rejected Transaction

```text
Enter withdrawal amount: 7000
Transaction rejected: Insufficient balance.
```

The withdrawal is rejected because the requested amount is greater than the available balance.

---

# 2. Student Grade Calculator

### Aim

To create a menu-driven student grade calculator that accepts marks in five subjects, calculates the average, and assigns a grade according to the given grading scheme.

### Grading Scheme

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A     |
| 75–89         | B     |
| 60–74         | C     |
| 40–59         | D     |
| Below 40      | F     |

### Logic

The program allows the user to enter marks for five subjects. It calculates the average by adding all five marks and dividing the total by five. The average is then compared with the grading scheme and the corresponding grade is displayed. The most recently entered student's information is stored so that it can be viewed later.

### Sample Input

```text
Enter marks for subject 1: 85
Enter marks for subject 2: 92
Enter marks for subject 3: 78
Enter marks for subject 4: 60
Enter marks for subject 5: 55
```

### Sample Output

```text
Student data saved successfully.

----- STUDENT DETAILS -----
Marks: [85.0, 92.0, 78.0, 60.0, 55.0]
Average: 74.0
Grade: C
```

### Invalid Input

```text
Enter marks for subject 1: 120
Marks must be between 0 and 100.
```

The program does not accept marks outside the range of 0 to 100.

---

# 3. Reverse Guessing Game

### Aim

To develop a game in which the computer guesses a number selected by the user using a binary-search style strategy.

### Logic

The user specifies a lower and upper limit and secretly selects a number within that range. The computer guesses the midpoint of the current range. Based on the user's response — `high`, `low`, or `correct` — the computer eliminates half of the possible numbers and continues guessing until the correct number is found.

### Sample Input

```text
Enter the lower limit: 1
Enter the upper limit: 100

My guess is: 50
Enter 'high', 'low', or 'correct': high

My guess is: 25
Enter 'high', 'low', or 'correct': low

My guess is: 37
Enter 'high', 'low', or 'correct': correct
```

### Sample Output

```text
I guessed your number!
Number of guesses: 3
```

### Invalid Input

```text
Enter 'high', 'low', or 'correct': abc
Invalid response. Please enter high, low, or correct.
```

---

# 4. Guessing Game with Hints and Scoring

### Aim

To create a guessing game in which the computer generates a random number and the user attempts to guess it using additional hints and a scoring system.

### Logic

The computer generates a random number between 1 and 100. The user starts with 100 points and loses 10 points for every incorrect guess. After each incorrect guess, the program gives hints about whether the number is higher or lower, whether it is even or odd, and whether it is a multiple of 5. The game ends when the user guesses correctly or reaches the maximum number of attempts.

### Sample Input

```text
Enter your guess: 50
Enter your guess: 75
Enter your guess: 72
```

### Sample Output

```text
Hint: Secret number is HIGHER.
Hint: Secret number is EVEN.
Hint: Secret number is NOT a multiple of 5.

Current Score: 90
Attempts left: 9

Congratulations! You guessed correctly.
Number of attempts: 3
Final Score: 80
```

### Invalid Input

```text
Enter your guess: abc
Please enter a valid number.
```

### Maximum Attempts Case

```text
You lost!
The secret number was: 64
Final Score: 0
```

---

# 5. Combined Application

### Aim

To combine the ATM Simulation, Student Grade Calculator, and Guessing Game into a single menu-driven Python application.

### Logic

The three individual programs are implemented as separate functions. A top-level menu allows the user to select ATM, Grade Calculator, or Guessing Game. Each function performs its own operations and uses `return` to give control back to the main menu instead of terminating the entire application.

### Sample Input

```text
==============================
       PYTHON LAB APP
==============================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit

Enter your choice: 1

Enter ATM PIN: 1234

Enter your choice: 5
```

### Sample Output

```text
==============================
       PYTHON LAB APP
==============================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit

Enter your choice: 1

----- ATM MENU -----
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Back to Main Menu

Enter your choice: 5

==============================
       PYTHON LAB APP
==============================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit
```

The program returns to the top-level menu after exiting the ATM section.

---

# Analysis

## 1. Why does b

