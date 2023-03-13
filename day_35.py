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

#extra
'''
function called find_index that takes two arguments; a list of integers, and an integer. 
The function should return the indexes of the integer in the list.
If the integer is not in the list, the function should convert all the numbers in the list into the given integer. 
For example, if the list is [1, 2, 4, 6, 7, 7] and the integer is 7, your code should return [4, 5] as the indexes 
of 7 in the list. If the list is [1, 2, 4, 6, 7, 7] and the integer is 8, 
your code should return [8, 8, 8, 8, 8, 8] because 8 is not in the list.
'''

def find_index(collection: list, number: int):
    indexes_of_number = []
    for index, value in enumerate(collection):
        if value == number:
            indexes_of_number.append(index)
    if not indexes_of_number:
        indexes_of_number = [number for x in range(len(collection))]
    return indexes_of_number


if __name__ == '__main__':
   
    #basic execute:
    example = 'the quick brown fox jumps over a lazy dog'   
    print(check_pangram(example))   #output: True

    #extra execute:
    collection = [1, 2, 4, 6, 7, 7]
    number_1 = 7
    number_2 = 8

    print(find_index(collection, number_1))
    print(find_index(collection, number_2))