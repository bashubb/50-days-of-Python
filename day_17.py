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


print(user_name())