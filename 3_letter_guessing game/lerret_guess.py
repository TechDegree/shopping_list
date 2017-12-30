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
    start = input("Press enter/return to start a new game.\nPress Q to quit\n>>> ")
    if start.lower() == "q":
        break

    # pick a random word
    random_number = random.randint(0, len(words)-1)
    random_word = words[random_number]
    print(random_word)

    # round up, so you can always be wrong at least 2 time
    max_wrong_guesses = math.ceil(len(random_word) // 3) + 1
    wrong_guesses = []
    guessed_letters = []

    # draw spaces for the word 
    print("_ " * len(random_word))

    word_not_guessed = True

    # guessing a word loop
    while word_not_guessed:

        # take a guess (letter)
        alphabat = string.ascii_lowercase
        guess = input("\nPlease choose a letter\n>>> ").lower()

        # add letters to guessed leters or increase wrong guesses
        if not guess.isalpha():
            print("You have to pick one letter only!")
            continue
        elif guess in wrong_guesses or guess in guessed_letters:
            print("You have already trued this one. Pick something else.")
            continue
        elif len(guess) != 1:
            print("You have to pick one letter only!")
            continue
        elif guess in random_word:
            for letter in random_word:
                if letter == guess:
                    guessed_letters.append(guess)
        else:
            wrong_guesses.append(guess)
            if max_wrong_guesses < len(wrong_guesses):
                print("You failed. My word was {}.\n".format(random_word))
                break
            print("Wrong guess. You have {}/{} wrong guesses.".format(len(wrong_guesses), max_wrong_guesses))

        # draw guessed letters and strikes
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        word_not_guessed = len(guessed_letters) < len(random_word) 
        
    else:
        print("\n")
    # give max number of wrong guesses based on len of the word
    # print out win/lose