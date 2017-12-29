import random
import string
import math

# make a list of word
words = [
    "apple",
    "banana",
    "orange",
    "coconut",
    "strawberry",
    "lime",
    "grapefruit",
    "lemon",
    "kumquat",
    "blueberry",
    "melon",
    "raspberry",
    "avocado",
    "squash",
    "pineapple"
]

# game loop
while True:
    start = input("Press enter/return to start, or enter Q to quit\n>>> ")
    if start.lower() == "q":
        break

    # pick a random word
    random_number = random.randint(0, len(words)-1)
    random_word = words[random_number]

    # round up, so you can always be wrong at least 1 time
    max_wrong_guesses = math.ceil(len(random_word // 3)) 
    wrong_guesses = 0

    # draw spaces for the word 
    print("_ " * len(random_word))

    # take a guess (letter)
    alphabat = string.ascii_lowercase
    guess = input("Please choose a letter from English alphabet").lower()

    # draw guessed letters and strikes or add counter if error
    for letter in random_word:
        if letter == guess:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            
   
    # give max number of wrong guesses based on len of the word
    # print out win/lose