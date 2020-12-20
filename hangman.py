"""

A basic game of Hangman

Players must guess a hidden word within a set number of tries.
Players can only guess single alphabetic characters one single time.
The word should be chosen randomly from a list of words.

"""
# To do:
# Ask to play again at the end of a game
# Fill "words" with data from a larger source of words, like an online dictionary

# Maybe: Create GUI or Webapp version of this game

import random


def get_word():
    """Return a random word for the player to guess from a list"""
    words = ['Python', 'Programming', 'String',
             'Concatenate']  # Initial list for testing purposes
    return random.choice(words).upper()


def player_guess():
    """Have the player guess a single character that is in the target word"""
    while True:
        guess = input(
            'Please enter a letter that you think is in the word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            return guess
            break
        elif len(guess) != 1:
            print('Please enter a single character')
        elif not guess.isalpha():
            print('No numbers allowed!')


def play_game():
    """The game funcion, where a player can play full game of text based Hangman"""
    strikes = 5
    word_to_guess = get_word()
    # Obfuscated version of word_to_guess to be displayed to the player.
    guessed = '*' * len(word_to_guess)
    # Any incorrectly guessed letters are appended to this list.
    list_of_guesses = []

    print("WELCOME TO HANGMAN \nTry to guess the word \n5 Strikes and you're out!")
    print('')
    print(f'Your word is {len(word_to_guess)} letters long. Try to guess it!')

    while strikes > 0:

        guess = player_guess()

        if guess in word_to_guess:
            print(f'Nice one! {guess} is in the word!')
            for char in word_to_guess:
                if char == guess:
                    word_to_guess.replace(char, '')
            list_of_guesses.append(guess)
            # Replace the '*' in guessed to the player's guess as per our word_to_guess:
            new_guessed = '' # Create new string to work with (strings are immutable) 
            for index, char in enumerate(word_to_guess): # Enumerate through characters in word.
                if char == guess: 
                    new_guessed += char # If the char matches the player's guess, append it to new_guessed.
                else:
                    new_guessed += guessed[index] # If the char does not match, append whatever is in guessed to new_guessed at its original index.
            guessed = new_guessed # Now we can use the variable "guessed" again.
            print(guessed)
            if guessed == word_to_guess:
                print(f'You have guessed the word "{word_to_guess}" and have won the game!')
                break
        elif guess not in word_to_guess:
            strikes -= 1
            list_of_guesses.append(guess)
            if strikes == 0:
                print(
                    f'You have {strikes} guess(es) left and have lost the game! Better luck next time!')
                print(f'The word was "{word_to_guess}"')
            else:
                print(f'Sorry, but "{guess}" is incorrect. Try again.')
                print('')
                print(f'You have {strikes} guesses left!')
                print('')
                print(f"Guesses made so far: {' '.join(list_of_guesses)}")
    

play_game()
