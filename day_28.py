#day 28
#basic:
'''
function called index_position. This function takes a string as a parameter and returns the positions,
or indexes, of all lowercase letters in the string. For example, "LovE" should return [1, 2].
'''

def index_position(sentence: str):
    index_of_lower = []
    for index, value in enumerate(sentence):
        if value.islower():
            index_of_lower.append(index) 
    return index_of_lower

#extra:
'''
function called largest_number that takes a list of integers and re-arranges the individual 
digits to create the largest number possible. For example, if you pass the following as an 
argument, list1 = [3, 67, 87, 9, 2]. Your code should return the number in this exact format: 
9,877,632 as the largest number.
'''

def largest_number(collection: list):
    pass