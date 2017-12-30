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
    start = input("Press enter/return to start a new game.\n Press enter Q to quit\n>>> ")
    if start.lower() == "q":
        break

    # pick a random word
    random_number = random.randint(0, len(words)-1)
    random_word = words[random_number]
    print(random_word)

    # round up, so you can always be wrong at least 1 time
    max_wrong_guesses = math.ceil(len(random_word) // 3) 
    wrong_guesses = 0
    guessed_letters = []

    # draw spaces for the word 
    print("_ " * len(random_word))

    word_not_guessed, can_guess_wrong = True, True

    # guessing a word loop
    while word_not_guessed and can_guess_wrong:


        # take a guess (letter)
        alphabat = string.ascii_lowercase
        guess = input("\nPlease choose a letter\n>>> ").lower()

        # add letters to guessed leters or increase wrong guesses
        if guess in random_word:
            for letter in random_word:
                if letter == guess:
                    guessed_letters.append(guess)
        else:
            wrong_guesses += 1
            print("Wrong guess. You have {}/{} wrong guesses.".format(wrong_guesses, max_wrong_guesses))
        
        # draw guessed letters and strikes or add counter if error
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        word_not_guessed = len(guessed_letters) < len(random_word) 
        can_guess_wrong = max_wrong_guesses >= wrong_guesses            
    print("\n")
    # give max number of wrong guesses based on len of the word
    # print out win/lose