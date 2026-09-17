```python
balance = 5000
pin = "1234"


def atm():
    global balance, pin

    entered_pin = input("Enter your PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN!")
        return

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance: ₹", balance)

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    print("Invalid amount!")
                else:
                    balance += amount
                    print("Amount deposited successfully.")
                    print("New Balance: ₹", balance)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount!")
                elif amount > balance:
                    print("Transaction rejected: Insufficient balance.")
                else:
                    balance -= amount
                    print("Please collect your cash.")
                    print("Remaining Balance: ₹", balance)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == "5":
            print("Thank you for using the ATM.")
            return

        else:
            print("Invalid choice!")


atm()
```
