from ps4a import (
    isValidWord, getWordScore, calculateHandlen, displayHand, loadWords,
    updateHand, playHand, HAND_SIZE, dealHand, d_si, List, Optional
)

# Computer chooses a word
def compChooseWord(hand: d_si, wordList: List[str], n: int) -> Optional[str]:
    """Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.
    
    This word should be calculated by considering all the words
    in the wordList.
    
    If no words in the wordList can be made from the hand, return None.
    
    returns: string or None

    Args:
        hand: dict of letter generate for a func
        wordList: all words acepted
        n: hand size 

    Returns:
        string or None
    """
    # Create a new variable to store the maximum score seen so far(initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > max_score):
                # update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    return best_word


# Computer plays a hand
def compPlayHand(hand: d_si, wordList: List[str], n: int) -> None:
    """Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.
    
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
    
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    Args:
        Args:
        hand: dict of letter generate for a func
        wordList: all words acepted
        n: hand size 
    
    Return:
        None:
    """
    # Keep track of the total score
    max_score = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        pc_word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if pc_word == None:
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(pc_word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the
                # updated total score 
                score = getWordScore(pc_word, n)
                max_score += score
                print(
                    f'"{pc_word}" earned {score} points. Total: {max_score}'
                                                                 + ' points\n')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, pc_word)
    # Game is over (user entered a '.' or ran out of letters), so tell user
    # the total score
    print(f'Total score: {max_score} points.')


# Problem #6: Playing a game
def playGame(wordList: List[str]):
    """Allow the user to play an arbitrary number of hands.
    
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
    
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.
    
    4) After the computer or user has played the hand, repeat from step 1
    """
    hand = {}
    while True:
        user_ans = input('\nEnter n to deal a new hand, r to replay the last'
                                                 + ' hand, or e to end game: ')
        if user_ans == 'n' or 'r':
            if len(hand) == 0:
                print('You have not played a hand yet. Please play a new hand'
                                                                  + 'first!\n')
                break
            if user_ans == 'n':
                hand = dealHand(HAND_SIZE)
            # get input on who is going to play the game (i.e you or computer)
            while True:
                who_play = input('\nEnter u to have yourself play, c to have'
                                                      + ' the computer play: ')
                if who_play in 'uc':
                    break
                else:
                    print('Invalid command.\n')
        
            if who_play == 'u':
                print()
                playHand(hand, wordList, HAND_SIZE)
            elif who_play == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
        
        elif user_ans == 'e':
            break
        
        else:
            print('Invalid command.')

        
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)