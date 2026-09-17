import random


# ---------------- ATM ----------------

balance = 5000
pin = "1234"


def atm():
    global balance, pin

    entered_pin = input("\nEnter ATM PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN!")
        return

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Balance: ₹", balance)

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    print("Invalid amount!")
                else:
                    balance += amount
                    print("Deposit successful.")
                    print("Balance: ₹", balance)

            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount!")
                elif amount > balance:
                    print("Transaction rejected: Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawal successful.")
                    print("Balance: ₹", balance)

            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("Invalid PIN format.")
            else:
                print("Incorrect PIN.")

        elif choice == "5":
            return

        else:
            print("Invalid choice!")


# ---------------- GRADE CALCULATOR ----------------

last_marks = None
last_average = None
last_grade = None


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def grade_calculator():
    global last_marks, last_average, last_grade

    while True:
        print("\n----- GRADE CALCULATOR -----")
        print("1. Enter marks")
        print("2. View last student's grade")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            marks = []

            for i in range(1, 6):
                while True:
                    try:
                        mark = float(input(f"Enter marks for subject {i}: "))

                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Invalid input!")

            average = sum(marks) / 5
            grade = calculate_grade(average)

            last_marks = marks
            last_average = average
            last_grade = grade

            print("Student data saved.")

        elif choice == "2":
            if last_marks is None:
                print("No student data available.")
            else:
                print("Marks:", last_marks)
                print("Average:", round(last_average, 2))
                print("Grade:", last_grade)

        elif choice == "3":
            return

        else:
            print("Invalid choice!")


# ---------------- GUESSING GAME ----------------

def guessing_game():
    secret = random.randint(1, 100)
    score = 100
    max_attempts = 10
    attempts = 0

    print("\n----- GUESSING GAME -----")
    print("Guess a number between 1 and 100.")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input!")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print("Congratulations! Correct guess.")
            print("Final Score:", score)
            return

        score -= 10

        if guess < secret:
            print("The number is higher.")
        else:
            print("The number is lower.")

        if secret % 2 == 0:
            print("Hint: Number is EVEN.")
        else:
            print("Hint: Number is ODD.")

        if secret % 5 == 0:
            print("Hint: Number is a multiple of 5.")
        else:
            print("Hint: Number is not a multiple of 5.")

    print("\nYou lost!")
    print("The secret number was:", secret)
    print("Final Score: 0")


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\n==============================")
        print("       PYTHON LAB APP")
        print("==============================")
        print("1. ATM")
        print("2. Grade Calculator")
        print("3. Guessing Game")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm()

        elif choice == "2":
            grade_calculator()

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()

