import random

secret = random.randint(1, 100)
valid_guesses = 0
invalid_guesses = 0

print("I'm thinking of a number from 1 to 100")

while True:
    guess = input("Try to guess my number: ")

    if not guess.isdigit():
        print(f"{guess} is not a valid guess - please guess again:")
        invalid_guesses += 1
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print(f"{guess} is not a valid guess - please guess again:")
        invalid_guesses += 1
        continue

    valid_guesses += 1

    if guess < secret:
        print(f"{guess} is too low - please guess again:")
    elif guess > secret:
        print(f"{guess} is too high - please guess again:")
    else:
        print(
            f"{guess} is correct! You guessed my number in "
            f"{valid_guesses} guesses and made {invalid_guesses} invalid guesses."
        )
        break