#!/usr/bin/env python3

# @author: danbros
# Pset3 do curso MITx: 6.00.1x (edX)
"""
Jogo da Forca

(Verifique se o arquivo "my_hangman.txt" está no mesmo dir que "my_hangman.py")
"""

import random
from pathlib import Path


def loadWords() -> list:
    """Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.

    Returns:
      list: Returns a list of valid words.
    """
    print("Loading word list from file...")
    # inFile: file
    print(WORDLIST_FILENAME)
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist: list) -> str:
    """Choose a word in wordlist
    
    Args:
        wordlist: list of words (strings)
    Returns:
        Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord: str, lettersGuessed: list) -> bool:
    """Verify if secretWord was guessed

    Args:
      secretWord: the word the user is guessing
      lettersGuessed: what letters have been guessed so far

    Returns:
        bool: True if all the letters of secretWord are in lettersGuessed,
        False otherwise
    """
    # return set(secretWord) <= set(lettersGuessed)
    return all(char in lettersGuessed for char in secretWord)
    

def getGuessedWord(secretWord: str, lettersGuessed: list) -> str:
    """Create a string with "-" in not guessed letters

    Args:
      secretWord: the word the user is guessing
      lettersGuessed: what letters have been guessed so far

    Returns:
        str: comprised of letters and underscores that represents what letters
        in secretWord have been guessed so far.
    """
    # Using ternary operator: ( [if True] [condition] [if False] ) [loop]
    # return ''.join(
    #    [char if char in lettersGuessed else '- ' for char in secretWord]
    #    )

    # Using ternary operator: ( [if False, if True] [condition] ) [loop]
    return ''.join(
        ['_ ', char] [char in lettersGuessed] for char in secretWord
        )


def getAvailableLetters(lettersGuessed: list) -> str:
    """Returns letter in alph not guessed

    Args:
      lettersGuessed: what letters have been guessed so far

    Returns:
        str: comprised of letters that represents what letters have not yet
        been guessed.
    """
    # Created alph 1, using list comprehesions
    # 97 is 'a' in ASCII code
    # compress_alp = ''.join([chr(97 + i) for i in range(26)])

    # Using alph 1
    # This not using ternary operator, but list comp sintax:
    # [return value] [for loop] [if filter]
    # return ''.join([e for e in compress_alp if e not in lettersGuessed])    

    # Or use oneline return
    # [return value] [ for loop [[r value] [for loop] ] [if filter]
    return ''.join(
        e for e in [chr(97 + i) for i in range(26)] if e not in lettersGuessed
        )


def hangman(secretWord: str):
    """Starts up an interactive game of Hangman.

    Args:
      secretWord: the secret word to guess.
    """
    mistakesMade = 0
    lettersGuessed = []  # type: list

    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')

    while True:
        print('-------------')

        if mistakesMade == 8:
            print('Sorry, you ran out of guesses. The word was else.')
            break

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        
        print(f'You have {8 - mistakesMade} guesses left.')
        
        availableLetters = getAvailableLetters(lettersGuessed)
        print(f'Available letters: {availableLetters}')

        guess_char = input('Please guess a letter: ').lower()

        gW = getGuessedWord

        if guess_char in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', 
                                                gW(secretWord, lettersGuessed))
        elif guess_char in secretWord:
            lettersGuessed.append(guess_char)
            print(f'Good guess:', gW(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess_char)
            print(f'Oops! That letter is not in my word:', 
                                                gW(secretWord, lettersGuessed))
            mistakesMade += 1


if __name__ == "__main__":

    WORDLIST_FILENAME = str(Path.cwd()) + "/my_hangman.txt"

    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)