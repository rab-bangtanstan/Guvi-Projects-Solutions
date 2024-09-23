import random

# Set the number to be guessed
number_to_guess = random.randint(1, 100)

print("Welcome to the 'Guess the Number' game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the player guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number:", number_to_guess)
        break
