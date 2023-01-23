#day 10:
#Basic challange:
'''
function called hide_password that takes no parameters. 
The function takes an input (a password) from a user and returns a hidden password. 
For example, if the user enters "hello" as a password, the function should return "****" 
as a password and tell the user that the password is 4 characters long.
'''


def hide_password():
    password = input("Please enter your password: ")
    password_lenght = len(password)
    hidden_password = ' '.join(['*' for x in range(password_lenght)])
    return f'Your hidden password is {hidden_password} and it is {password_lenght} long'


#Extra challange:
'''
Your new company has a list of figures saved in a database. 
The issue is that these numbers have no separator. 
The numbers are saved in a list in the following format: [1000000, 2356989, 2354672, 9878098]. 
You have been asked to write a code that will convert each of the numbers in the list into a string. 
Your code should then add a comma on each number as a thousand separator for readability. 
When you run your code on the above list, your output should be: [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’] 
Write a function called convert_numbers that will take one argument, the list of numbers above.
'''

def thousand_separator(collection: list):
    string_collection = [format(x, ',d') for x in collection]
    return string_collection
    


if __name__ == '__main__':

    print(hide_password())

    example = [1000000, 2356989, 2354672, 9878098]
    print(thousand_separator(example))
