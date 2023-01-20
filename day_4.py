# day 4th:
# basic challange: 
'''
function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, 
returns 1 if only one argument is a float, and returns 0 if neither argument is a float.
'''


def only_float(collection):
    number_of_floats = 0
    for number in collection:
        if type(number) == float:
            number_of_floats +=1
    return number_of_floats


# Extra Challenge: Index of the Longest Word
'''
a function called word_index that takes one argument, a list of strings, 
and returns the index of the longest word in the list. If there is 
no longest word (if all the strings are of the same length), the function should return zero (0).
 '''


def word_index(collection: list):
    longest_word = max(collection)
    if min(collection) == longest_word:
        return 0
    else:
        return collection.index(longest_word)



if __name__ == "__main__":    
    example = (12.1, 23)
    words1 = ["Hate", "remorse", "vengeance"]
    words2 = ["sun", "sun", "sun"]

    print(only_float(example))
    print(word_index(words1))
    print(word_index(words2))