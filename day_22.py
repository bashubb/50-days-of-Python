#day 22
#basic:
'''
Create three functions. The first, called add_hash takes a string and adds a hash (#) between the words. 
The second function, called add_underscore removes the hash (#) and replaces it with an underscore ("_"). 
The third function, called remove_underscore, removes the underscore and replaces it with nothing. 
If you pass "Python" as an argument for the three functions, and you call them at the same time like: 
print(remove_underscore(add_underscore(add_hash('Python')))) it should return "Python".
'''

def add_hash(word: str):
    word_with_hash = word.replace(' ', '#')
    return word_with_hash

def add_uderscore(word: str):
    word_with_uderscore = word.replace('#', '_')
    return word_with_uderscore
    

def remove_underscore(word: str):
    word_with_spaces = word.replace('_', ' ')
    return word_with_spaces
    

if __name__ == '__main__':

    #execution basic
    sentence = 'I love you'
    print(remove_underscore(add_uderscore(add_hash(sentence))))