# generate a random number between 1 and 10
# get a number from the player
# compare guess and secret number 
# prit hit/miss
# max 5 guesses

import random

def game():
    secret_number = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(input("What is your guess?\n>>> "))
        except ValueError:
            print("This is a NUMBER guessing game. Please give me a number!")
        else:   
         
            if guess == secret_number:
                print("Correct! {} is the secret number!".format(guess))
                break
            else:
                print("I am sorry, {} is not the correct number".format(guess))
            guesses.append(guess)
    else:
        print("You run out of guesses. My secret number was {}.".format(secret_number))

    play_again = input("\nDo you want to play again? Y/n?\n>>> ")
    if play_again.lower() != "n":
        game()
    else:
        print("Thanks for playing. See ya!")

game()
