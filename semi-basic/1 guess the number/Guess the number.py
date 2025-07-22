import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 6
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
            continue
            
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue
            
        attempts -= 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            return
        elif guess < secret_number:
            print(f"Your guess is too low. Attempts remaining: {attempts}")
        else:
            print(f"Your guess is too high. Attempts remaining: {attempts}")
    
    print(f"\nGame over! You ran out of attempts. The number was {secret_number}.")

# Start the game
guess_the_number()