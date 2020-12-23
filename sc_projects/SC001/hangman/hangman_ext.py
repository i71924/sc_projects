"""
File: hangman.py
Name: Po Kai Feng
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    First print the dashed_word based on the length of answer.
    While user give a legal guess, check if the guess character is in answer.
    If the guess is correct, uncover the dashed_word with the guess.
    Or if the guess is wrong, makes guess_times plus one.
    While there were no dash in dashed_word or there is no chance to try, end game
    and show whether user win or lose and print the answer
    """
    answer = random_word().upper()
    dashed_word = ''
    for i in range(len(answer)):
        dashed_word += '-'
    guess_times = 0
    while True:
        if guess_times == N_TURNS:
            # This is the last chance to guess and user failed
            print('You are completely hung :\'(')
            break
        print('The word looks like: ' + dashed_word + '\nYou have ' + str(N_TURNS - guess_times) + ' guesses left.')
        guess = input('Your Guess: ')
        if len(guess) == 1 and guess.isalpha():
            # Legal format
            guess = guess.upper()
            if answer.find(guess) != -1:
                # The guess is correct and should uncover the dashed_word
                print('You are correct!')
                dashed_word = uncover_dash(guess, answer, dashed_word)
                if not dashed_word.find('-') > -1:
                    # No dash left.
                    print('You win!!')
                    break
            else:
                # Wrong guess
                guess_times += 1
                print('There is no ' + guess + '\'s in the word.')
            print_hangman(guess_times)
        else:
            print('Illegal format')
    print('The word was: ' + answer)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def uncover_dash(guess, answer, dashed_word):
    """
    :param guess: str, the character that user type and has been converted to upper case
    :param answer: str, the answer word
    :param dashed_word: str, the present dashed_word
    :return: str, the new_dashed_word with all correct guess been shown in dashed_word
    """
    new_dashed_word = ''
    for i in range(len(answer)):
        if guess == answer[i]:
            new_dashed_word += guess
        else:
            new_dashed_word += dashed_word[i]
    return new_dashed_word


def print_hangman(guess_times):
    """
    :param guess_times: how many times user has guessed
    print the picture of hangman differed by the number of guess_times like the following:
    __________
    |    |
    |  (O_O)
    |  / | \
    |    |
    |   / \
    ----------
    """
    for i in range(7):
        for j in range(10):
            if i == 0:
                print('-', end='')
            elif i == 1:
                if j == 0:
                    print('|', end='')
                elif j == 5 and guess_times > 0:
                    print('|', end='')
                else:
                    print(' ', end='')
            elif i == 2:
                if j == 0:
                    print('|', end='')
                elif j == 3 and guess_times > 1:
                    print('(', end='')
                elif (j == 4 or j == 6) and guess_times > 1:
                    if guess_times == N_TURNS:
                        print('#', end='')
                    else:
                        print('O', end='')
                elif j == 5 and guess_times > 1:
                    print('_', end='')
                elif j == 7 and guess_times > 1:
                    print(')', end='')
                else:
                    print(' ', end='')
            elif i == 3:
                if j == 0:
                    print('|', end='')
                elif j == 3 and guess_times > 3:
                    print('/', end='')
                elif j == 5 and guess_times > 2:
                    print('|', end='')
                elif j == 7 and guess_times > 4:
                    print('\\', end='')
                else:
                    print(' ', end='')
            elif i == 4:
                if j == 0:
                    print('|', end='')
                elif j == 5 and guess_times > 2:
                    print('|', end='')
                else:
                    print(' ', end='')
            elif i == 5:
                if j == 0:
                    print('|', end='')
                elif j == 4 and guess_times > 5:
                    print('/', end='')
                elif j == 6 and guess_times > 6:
                    print('\\', end='')
                else:
                    print(' ', end='')
            elif i == 6:
                print('-', end='')
        print('')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
