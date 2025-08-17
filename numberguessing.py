import random

def number_guessing_game():
    """A simple number guessing game."""
    secret_number = random.randint(1, 100)
    guess_count = 0
    
    print("Guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! The number was {secret_number}.")
                print(f"You guessed it in {guess_count} tries.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- Run Program ---
number_guessing_game()
