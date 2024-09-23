import random

print("Welcome to the Dice Roll Simulator!")

while True:
    roll = input("Press 'r' to roll the dice or 'q' to quit: ").lower()

    if roll == 'r':
        result = random.randint(1, 6)
        print("You rolled a", result, "!")
    elif roll == 'q':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please press 'r' to roll or 'q' to quit.")
