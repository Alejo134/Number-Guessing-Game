import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

difficulty = input("Enter the difficulty level (1, 2, or 3): ")
chances = 0
while difficulty not in ["1", "2", "3"]:
    difficulty = input("Invalid input. Please select a valid difficulty level (1, 2, or 3): ")
    
    
    
if difficulty == "1":
        chances = 10
elif difficulty == "2":
        chances = 5
elif difficulty == "3":
        chances = 3

print("You have selected difficulty level " + difficulty + " you have " + str(chances) + " chances to guess the number.")


 
numero = random.randint(1, 100)
guess = 0
chancesTotales = chances

print("Let's start the game!")
while numero != guess and chancesTotales > 0:
    guess = int(input("Enter your guess: "))
    chancesTotales -= 1
    
    if guess < numero:
        print("Incorrect. The number is greater than " + str(guess) + ". Try again.")
    elif guess > numero:
        print("Incorrect. The number is less than " + str(guess) + ". Try again.")
    else:
        print("Congratulations! You've guessed the number in " + str(chances - chancesTotales) + " tries!")
        break
