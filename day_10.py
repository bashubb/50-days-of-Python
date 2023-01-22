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


if __name__ == '__main__':

    print(hide_password())