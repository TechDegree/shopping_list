import random

def game():
    secret_number = random.randint(1, 10) # generate a random number between 1 and 10
    guesses = []

    while len(guesses) < 5: #limit guesses to 5
        try: 
            guess = int(input("What is your guess?\n>>> ")) # get a number from the player
        except ValueError:
            print("This is a NUMBER guessing game. Please give me a number!") # catch non numbers
        else:   
         
            if guess == secret_number:
                print("Correct! {} is the secret number!".format(guess))
                break
            else:
                print("I am sorry, {} is not the correct number".format(guess))
            guesses.append(guess)
    else:
        print("You run out of guesses. My secret number was {}.".format(secret_number))

    # let player play again
    play_again = input("\nDo you want to play again? Y/n?\n>>> ")
    if play_again.lower() != "n":
        game()
    else:
        print("Thanks for playing. See ya!")

game()
