# day 4th:
# basic challange: 

def only_float(collection):
    number_of_floats = 0
    for number in collection:
        if type(number) == float:
            number_of_floats +=1
    return number_of_floats

# Extra Challenge: Index of the Longest Word


def word_index(collection: list):
    longest_word = max(collection)
    if min(collection) == longest_word:
        return 0
    else:
        return collection.index(longest_word)


    
        
example = (12.1, 23)
words1 = ["Hate", "remorse", "vengeance"]
words2 = ["sun", "sun", "sun"]

print(only_float(example))
print(word_index(words1))
print(word_index(words2))