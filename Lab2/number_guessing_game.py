# This program is a number guessing game with a maximum of 7 attempts.

import random

secret_number = random.randint(1, 100)
max_attempts = 7

print("Guess the number between 1 and 100.")
print("You have", max_attempts, "attempts.")

for attempt in range(1, max_attempts + 1):

    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct!")
        print("You guessed the number in", attempt, "attempt(s).")
        break

else:
    print("You have used all your attempts.")
    print("The correct number was", secret_number)
