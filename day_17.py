#day 17:
#basic challange:
'''
function called user_name, that creates a username for the user. 
The function should ask a user to input their name. 
The function should then reverse the name and attach a randomly issued number between 0 and 9 at the end of the name. 
The function should return the username.
'''
from random import randint, randrange

def user_name():
    name = input("Please enter your name ")
    new_name = name[::-1] + str(randrange(10))
    return new_name



#extra challange
'''
names = [ "Peter", "Jon", "Andrew"] 
Write a function called sort_length that takes a list of strings as an argument 
and sorts the strings in ascending order according to their length. For example,
the list above should return: ['Jon', 'Peter', 'Andrew'] Do not use the built-in sort functions.
'''

def sort_length (collection: list):
    for index in range(len(collection) - 1):
        if len(collection[index]) > len(collection[index+1]):
            a, b = index, index+1
            collection[b], collection[a] = collection[a], collection[b]
    return collection


if __name__ == '__main__':

    #execution basic
    print(user_name())

    #execution extra
    names = [ "Peter", "Jon", "Andrew"] 
    print(sort_length(names))