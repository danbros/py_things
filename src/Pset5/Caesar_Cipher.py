#!/usr/bin/env python3

# author @danbros
# Pset5 do curso MITx: 6.00.1x (edX)

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name: list) -> list:
    """Depending on the size of the word list, this function may take a while
    to finish.

    Args:
        file_name: the name of the file containing the list of words to load

    Returns:
        list: a list of valid words. Words are strings of lowercase letters.
    """
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list: list, word: str) -> bool:
    """
    Determines if word is a valid word, ignoring capitalization and punctuation
    
    Example:
        is_word(word_list, 'bat') returns True
        is_word(word_list, 'asdf') returns False

    Args:
        word_list: list of words in the dictionary.
        word: a possible word.

    Returns:
        bool: True if word is in word_list, False otherwise
    """
    word = word.lower()
    word = word.strip(r" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string() -> str:
    """Returns: a joke in encrypted text."""
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text: str):
        """Initializes a Message object
                
        Args:
            text: the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self) -> str:
        """Used to safely access self.message_text outside of the class
        
        Returns:
            str: self.message_text
        """
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self) -> list:
        """
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns:
            list: a COPY of self.valid_words
        """
        return self.valid_words[:]
        
    def build_shift_dict(self, shift: int) -> dict:
        """Creates a dictionary that can be used to apply a cipher to a letter.

        The dictionary maps every uppercase and lowercase letter to a character
        shifted down the alphabet by the input shift. The dictionary should
        have 52 keys of all the uppercase letters and all the lowercase letters
        only.

        Args:
            shift(int): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns:
            dict: a dictionary mapping a letter (string) to another letter
            (string).
        """
        alph_lower = [chr(97 + i) for i in range(26)]
        alph_upper = [s.upper() for s in alph_lower]
        
        shift_lower = alph_lower[shift:] + alph_lower[:shift]
        shift_upper = alph_upper[shift:] + alph_upper[:shift]
        
        full_alph = alph_lower + alph_upper
        full_shift = shift_lower + shift_upper

        self.shift_dict = dict(zip(full_alph, full_shift))

        return self.shift_dict

    def apply_shift(self, shift: int) -> str:
        """Applies the Caesar Cipher to self.message_text with the input shift.

        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift
        
        Args:
            shift(int): the shift with which to encrypt the message.
            0 <= shift < 26

        Returns:
            str: the message text (string) in which every character is shifted
            down the alphabet by the input shift
        """
        s_dict = self.build_shift_dict(shift)

        ans = (s_dict[i] if i in s_dict else i for i in self.message_text)
        # ans = []
        # for i in self.message_text:
        #     if i in s_dict:
        #         ans.append(s_dict[i])
        #     else:
        #        ans.append(i) 
        return ''.join(ans)


class PlaintextMessage(Message):
    def __init__(self, text: str, shift: int):
        """Initializes a PlaintextMessage object
    
        A PlaintextMessage obj inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
    
        Hint: consider using the parent class constructor so less
        code is repeated

        Args:
            text(str): the message's text
            shift(int): the shift associated with this message
        """
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)

    def get_shift(self) -> int:
        """Used to safely access self.shift outside of the class
        
        Returns:
            int: self.shift
        """
        return self.shift

    def get_encrypting_dict(self) -> dict:
        """Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns:
            dict: a COPY of self.encrypting_dict
        """
        return dict(self.encrypting_dict)

    def get_message_text_encrypted(self) -> str:
        """
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns:
            str: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift: int) -> None:
        """Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).
        
        Args:
            shift(int): the new shift that should be associated with this
            message. 0 <= shift < 26 

        Returns:
            None:
        """
        self.shift = shift
        self.encrypting_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text: str):
        """Initializes a CiphertextMessage object
    
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)

        Args:
            text(str): the message's text
        """
        super().__init__(text)

    def decrypt_message(self) -> tuple:
        """Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.
        
        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        
        Returns:
            tuple: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        # This was work one time, after only work sometimes
        # I cannot make this work, maybe the problema not is here
        w_count = 0
        max_count = 0

        for i in range(26):
            msg = (self.apply_shift(i).split(' '))
            for w in msg:
                if is_word(self.valid_words, w):
                    w_count += 1
            if w_count > max_count:
                max_count = w_count
                key = i

        return (key, self.apply_shift(key))


def decrypt_story():
    """Load the file store.txt, and decript it"""
    return CiphertextMessage(get_story_string()).decrypt_message()


WORDLIST_FILENAME = 'words_Ccipher.txt'


if __name__ == "__main__":
    print(decrypt_story())