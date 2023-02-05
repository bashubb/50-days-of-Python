#day 19
# basic:
'''
Write two functions. The first function is called count_words which takes 
a string of words and counts how many words are in the string. 
The second function, called count_elements takes a string of words 
and counts how many elements are in the string. Do not count the whitespaces. 
The first function will return the number of words in a string, and the second one 
will return the number of elements (less whitespace). If you pass "I love learning," 
the count_words function should return 3 words and count_elements should return 13 elements.
'''

def count_words(sentence: str):
    how_many_words = len(sentence.split())
    return f'There is {how_many_words} words in the input sentence'
    

def count_elements(sentence: str):
    counter = 0 
    for element in sentence:
        if element.isalpha():
            counter += 1
    return counter


if __name__ == '__main__':

    #execute basic
    example_sentence = "I love learning,"
    print(count_words(example_sentence))
    print(count_elements(example_sentence))

    