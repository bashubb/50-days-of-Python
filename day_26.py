# day 26 
# basic:
'''
a function called sort_words that takes a string of words as an argument,
removes the whitespaces, and returns a list of letters sorted in alphabetical order. 
Letters will be separated by commas. All letters should appear once in the list. 
This means that you sort and remove duplicates. For example, "love life" should return as ['e, f, i, l, o, v'].
'''

def sort_words(sentence: str):
    list_letters = [letter for letter in sentence if letter != ' ']
    no_duplicates = list(set(list_letters))
    no_duplicates.sort() 
    return no_duplicates


# extra:
'''
s = 'Hi my name is Richard' 
Write a function called string_length that takes a string of words 
(words and spaces) as argument. This function should return the length of 
all the words in the string. Return the results in the form of a dictionary.
The string above should return: {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
'''

def string_lenght(sentence: str):
    list_of_words = sentence.split()
    len_dict = {}
    for word in list_of_words:
        len_dict[word] = len(word)
    return len_dict


if __name__ == '__main__':
    # basic execution:
    example = "love life"  
    print(sort_words(example))  # output : ['e, f, i, l, o, v']

    #extra execution:
    s = 'Hi my name is Richard' 
    print(string_lenght(s))
    
