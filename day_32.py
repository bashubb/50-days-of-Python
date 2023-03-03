#day 32
#basic:
'''function called password_validator. 
The function asks the user to enter a password.
A valid password should have at least one uppercase letter, 
one lowercase letter, and one number. It should not be less than 8 characters long.
When the user enters a password, the function should check if the password is valid. 
If the password is valid, the function should return the valid password.
If the password is not valid, the function should inform the user of the errors in 
the password and prompt the user to enter another password.
The code should only stop once the user enters a valid password. (use while loop).
'''

def welcome():
    print('''
                        ================ Welome in app pasword validator.  ================
                              This program going to check if password is valid or no.
                            A valid password should have at least one uppercase letter, 
                one lowercase letter, and one number. It should not be less than 8 characters long.'''  )


def enter_password():
    password = input('Please enter your password: ')
    return password

def valid_check():
    password = enter_password()
    lenght = True
    number = 0
    lower = 0
    upper = 0
    for letter in password:
        if letter.isnumeric():
            number += 1
        if letter.isupper():
            upper += 1
        if letter.islower():
            lower += 1
    if len(password) < 8:
        lenght = False
    
    if lenght and number and lower and upper:
        valid = True
    else:
        valid = False
    
    return valid, password
     

def password_validator():       #main function
    welcome()
    while True:
        check_if_valid = valid_check()
        valid = check_if_valid[0]
        password = check_if_valid[1]
        if valid:
            return password
        else:
            print('\nYour password is not valid, please try again.')


if __name__ == '__main__':

    #execute basic: 
    password_validator()
    
