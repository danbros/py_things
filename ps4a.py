#!/usr/bin/env python3

# author @danbros
# Pset4 do curso MITx: 6.00.1x (edX)

import random
from typing import Union, Dict, List, Optional

d_si = Dict[str, int]

def loadWords() -> List[str]:
    """Load the file with words.
    
    Returns:
        list: list of valid words
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")

    return wordList


def getFrequencyDict(sequence: Union[str, list]) -> d_si:
    """Convert a string/list to a dict (k = letter, v = num of letter freq)

    Args:
        sequence: words to be converted in dict freq

    Returns:
        Dict[str, int]: a dictionary where the keys are elements of the
        sequence and the values are integer counts, for the number of times
        that an element is repeated in the sequence.
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# Problem #1: Scoring a word
def getWordScore(word: str, n: int) -> int:
    """Returns the score for a word. Assumes the word is a valid word.
    
    The score for a word is the sum of the points for letters in the word, 
    multiplied by the length of the word, PLUS 50 points if all n letters are
    used on the first turn.
    
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth
    3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    Args:
        word: lowercase letters
        n: hand size

    Returns:
        int: score of word
    """
    # (SCRABBLE_LETTER_VALUES[char]) rise a exception if char not in SCRABBL...
    ans = sum(SCRABBLE_LETTER_VALUES.get(char, 0) for char in word) * len(word)

    #  [if False, if True] [condition]  (ternary op)
    return [ans, ans + 50] [len(word) == n]

# Problem #2:Make sure you understand how this function works and what it does!
def displayHand(hand: d_si) -> None:
    """Displays the letters currently in the hand.

    Args:
        hand: letters in a hand ({'a':1, 'x':2, 'l':3, 'e':1})

    Returns:
        None: (but print('a, x, x, l, l, l, e')).
    """
    for letter in hand.keys():
        for _ in range(hand[letter]):
            print(letter,end=" ")
    print()                             


# Problem #2:Make sure you understand how this function works and what it does!
def dealHand(n: int) -> d_si:
    """Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    
    Hands are represented as dictionaries. The keys are letters and the values
    are the number of times the particular letter is repeated in that hand.

    Args:
        n: int >= 0, number of cards to keep in the hands

    Returns:
        Dict[str, int]: random dict of letter of "deck"
    """
    hand = {}  # type: Dict [str, int]
    numVowels = n // 3

    for _ in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for _ in range(numVowels, n): # Or (n - numVowels)
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


# Problem #2: Update a hand by removing letters
def updateHand(hand: d_si, word: str) -> d_si:
    """Update hand, del all letter in word from hand
    
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    
    Has no side effects: does not modify hand.

    Args:
        hand: All letter in your hand
        word: word formed by player

    Returns:
        Dict[str, int]: new hand, without those int values from letters in it. 
    """
    cp_hand = hand.copy()

    for char in word:
        cp_hand[char] = cp_hand.get(char, 0) - 1
    return cp_hand
    # One line:
    # return {char: hand[char] - word.count(char) for char in hand} # Kiwitrade


# Problem #3: Test word validity
def isValidWord(word: str, hand: Dict[str, int], wordList: List[str]) -> bool:
    """Verify if word answer is in wordList and in hand
    
    Does not mutate hand or wordList.

    Args:
        word: guest user
        hand: current letter in a hand
        wordList: valid list of all words

    Returns:
        bool: True if word is in the wordList and is entirely
        composed of letters in the hand. Otherwise, returns False.
    """
    cp_hand = hand.copy()

    if word not in wordList:
        return False

    for char in word:
        if cp_hand.get(char, 0) < 1:
            return False
        else:
            cp_hand[char] = cp_hand.get(char,0) - 1

    return True
    # one line:
    # return word in wordList and all(word.count(c) <= hand.get(c, 0) 
    #                                               for c in word) # Kiwitrader

# Problem #4: Playing a hand
def calculateHandlen(hand: Dict[str, int]) -> int:
    """Calculate hand length
    
    Args:
        hand: 

    Returns:
        int: the length (number of letters) in the current hand.
    """
    return sum(hand.values())


# Problem #4: Playing a hand
def playHand(hand: Dict[str, int], wordList: List[str], n: int) -> None:
    """Allows the user to play the given hand, as follows:
    
    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

    Args:
        hand: dict of letter generate for a func
        wordList: all words acepted
        n: hand size

    Returns:
        None:
    """
    # Keep track of the total score
    score = 0
    cp_hand = hand.copy()

    # As long as there are still letters left in the hand:
    while calculateHandlen(cp_hand) > 0:
        # Display the hand
        print('Current Hand: ', end = " ") 
        displayHand(cp_hand)
        # Ask user for input
        user_ans = input(
                    'Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if user_ans == '.':
            # End the game (break out of the loop)
            break  
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(user_ans, cp_hand, wordList):
                # Reject invalid word(print a message followed by a blank line)
                print('Invalid word, please try again.\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the
                # updated total score, in one line followed by a blank line
                score += getWordScore(user_ans, n)

                print(f'"{user_ans}" earned {getWordScore(user_ans, n)} '
                + f'points. Total: {score} points\n')

                # Update the hand 
                cp_hand = updateHand(cp_hand, user_ans)
            
    # Game is over (user entered a '.' or ran out of letters), so tell user
    # the total score
    if user_ans == ".":
        print(f'Goodbye! Total score: {score}')
    else:
        print(f'Run out of letters. Total score: {score}\n')


# Problem #5: Playing a game
def playGame(wordList: List[str]) -> None:
    """Allow the user to play an arbitrary number of hands.
    
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'n', let the user play a new (random) hand.
        * If the user inputs 'r', let the user play the last hand again.
        * If the user inputs 'e', exit the game.
        * If the user inputs anything else, tell them their input was invalid.
    
    2) When done playing the hand, repeat from step 1

    Args:
        wordList: list with all words playable

    Returns:
        None
    """
    hand = {}
    while True:
        user_ans = input('\nEnter n to deal a new hand, r to replay the last'
                                                  + 'hand, or e to end game: ')
        if user_ans == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)

        elif user_ans == 'e':
            break
        elif user_ans == 'r':
            if len(hand) == 0:
                print('You have not played a hand yet. Please play a new hand'
                                                                    + 'first!')
            else:
                playHand(hand, wordList, HAND_SIZE)  
        else:
            print('Invalid command.')


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = 'words.txt'


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)