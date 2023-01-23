#day 11:
#Basic challange:
'''
function called equal_strings. The function takes two strings as arguments
and compares them. If the strings are equal (if they have the same characters and have equal length),
it should return True; if they are not, it should return False. For example, "love" and "evol" should return True.
'''

def equal_strings(first_word, second_word: str):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False

# Extra challange:
'''
function called swap_values. 
This function takes a list of numbers and swaps the first element with the last element. 
For example, if you pass [2, 4, 67, 7] as a parameter, your function should return. [7, 4, 67, 2].
'''

def swap_values(collection: list):
    last_to_first = collection.pop()
    collection.append(collection.pop(0))
    collection.insert(0, last_to_first)
    return collection


if __name__ == '__main__':

    print(equal_strings("love", "evol"))

    example = [2, 4, 67, 7]
    print(swap_values(example))

