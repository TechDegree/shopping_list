# generate a random number between 1 and 10 
# get a number from the player 
# compare guess and secret number  
# prit hit/miss

import random 
 
secret_number = random.randint(1, 10) 
 
while True: 
    guess = int(input("What is your guess?\n>>> ")) 
 
    if guess == secret_number: 
        print("Correct! {} is the secret number!".format(guess)) 
        break 
    else: 
        print("I am sorry, {} is not the correct number".format(guess))
