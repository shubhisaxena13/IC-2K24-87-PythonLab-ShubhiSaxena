def reverse_guessing_game():
    print("\n----- REVERSE GUESSING GAME -----")

    try:
        low = int(input("Enter the lower limit: "))
        high = int(input("Enter the upper limit: "))

        if low >= high:
            print("Invalid range!")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    guesses = 0

    print(f"\nThink of a number between {low} and {high}.")
    print("I will try to guess it.")

    while low <= high:
        guess = (low + high) // 2
        guesses += 1

        print("\nMy guess is:", guess)
        response = input("Enter 'high', 'low', or 'correct': ").lower()

        if response == "correct":
            print("I guessed your number!")
            print("Number of guesses:", guesses)
            return

        elif response == "low":
            low = guess + 1

        elif response == "high":
            high = guess - 1

        else:
            print("Invalid response. Please enter high, low, or correct.")

    print("Your responses were inconsistent.")


reverse_guessing_game()
