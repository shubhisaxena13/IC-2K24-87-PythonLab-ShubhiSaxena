import random


def guessing_game():
    secret = random.randint(1, 100)

    score = 100
    max_attempts = 10
    attempts = 0

    print("\n----- GUESSING GAME -----")
    print("Guess a number between 1 and 100.")
    print("You have 10 attempts.")
    print("Starting score: 100")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print("\nCongratulations! You guessed correctly.")
            print("Number of attempts:", attempts)
            print("Final Score:", score)
            return

        score -= 10

        if guess < secret:
            print("Hint: Secret number is HIGHER.")
        else:
            print("Hint: Secret number is LOWER.")

        if secret % 2 == 0:
            print("Hint: Secret number is EVEN.")
        else:
            print("Hint: Secret number is ODD.")

        if secret % 5 == 0:
            print("Hint: Secret number is a MULTIPLE of 5.")
        else:
            print("Hint: Secret number is NOT a multiple of 5.")

        print("Current Score:", score)
        print("Attempts left:", max_attempts - attempts)

    print("\nYou lost!")
    print("The secret number was:", secret)
    print("Final Score: 0")


guessing_game()
