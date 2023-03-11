#day 35 
#basic:
'''
function called check_pangram that takes a string and checks if it is a pangram. 
A pangram is a sentence that contains all the letters of the alphabet. 
If it is a pangram, the function should return True, otherwise, it should return return False.
The following sentence is a pangram, so it should return True: 'the quick brown fox jumps over a lazy dog'
'''

import string 

def check_pangram(sentence: str):
    alphabet = list(string.ascii_lowercase)
    for letter in sentence:
        if letter.lower() in alphabet:
            alphabet.remove(letter.lower())
    if alphabet == []:
        return True
    else:
        return False

if __name__ == '__main__':
   
    #basic execute:
    example = 'the quick brown fox jumps over a lazy dog'   
    print(check_pangram(example))   #output: True