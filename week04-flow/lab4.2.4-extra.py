import random

# Generate a random number between 0 and 100
secret_number = random.randint(0, 100)

# Initialize the number of attempts
attempts = 0

# Use a while loop to keep prompting the user
while True:
    # Ask the user to guess the number
    guess = int(input("guess the number: "))
    attempts += 1  # Increment the number of attempts

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  # Exit the loop
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")