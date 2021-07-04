import os
from platform import system
import random
import time

# Clear Terminal Function
def clear():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Win state
def win(num, guesses, score):
    print(f"You guessed the number!\nThe Number: {num}\nNumber of Guesses: {guesses}\nScore: {score}/10.")
    time.sleep(1)
    exit()

# Lose state
def lose(number):
    print(f"You lost. The number was {number}.\nAs you lost, your score is a whopping...")
    time.sleep(3)
    print("Zero!")
    exit()

# Types of clues. Can add more in the future.
clues = [
    "higher/lower",
    "odd/even"
]

# Can change this line to alter the number of tries.
tries = 10

# Starting the score with the number of tries then decrementing it on every wrong guess.
score = tries

# Generating the random number.
number = random.randint(1, 100)

# Starting
print(f"- You have to guess a number between 1 and 100.\n- You have {tries} tries to guess the number.\n- You will have 3 seconds to read each clue.\nAre you ready? (Press Enter to start)")

# Asking if the person is ready or not.
ready = input()
if ready != "":
    exit()

# Actual guesses.
for i in range(tries):
    # Clearing the terminal after each guess.
    clear()
    
    # Displays the score
    sc = f"Score: {score}"
    print(sc.rjust(os.get_terminal_size().columns-1))
    
    # Taking the guess from the user.
    try:
        guess = int(input("Enter a guess: "))
    except ValueError:
        # Disqualifying if invalid number is sent.
        print("You didn't send a valid number. Disqualified.")
        time.sleep(1)
        exit()
    else:
        # Win condition
        if guess == number:
            # Special Line if the person somehow guesses it on the 1st try. (1/100 chance)
            if i == 0:
                print("Damn! 1st try!")
            # Running the win condition.
            win(number, i+1, score)
        # Wrong Guess
        elif not i == tries-1: # Have the if condition here to not print clue on last guess.
            score -= 1 # Decrementing the score.
            print("Nope.")
            clue = random.choice(clues) # Choosing the type of the clue.
            if clue == "odd/even":
                clues.remove(clue) # Removing the odd/even clue type as its a one time clue.
                clue = "The number is even" if number % 2 == 0 else "The number is odd."
            else:
                clue = "What you guessed is higher than the number." if guess > number else "What you guessed is lower than the number."
            print(f"Clue is: {clue}")
            time.sleep(3)
else:
    # Running the losing condition.
    lose(number)