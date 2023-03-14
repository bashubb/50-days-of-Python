#day 36
#basic:
'''
a function called count that takes one argument a string, 
and returns a dictionary of how many times each element appears in the string.
For example, 'hello' should return: {'h':1,'e': 1,'l':2, 'o':1}.
'''

def count(sentence: str):
    count_letters = {}
    for letter in sentence:
        if letter not in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1
    return count_letters

if __name__ == '__main__':

    #basic execution:
    example = 'hello'
    print(count(example))   #output: {'h':1,'e': 1,'l':2, 'o':1}
