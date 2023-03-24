#day 39
'''
function called generate_password that generates any length of password for the user. 
The password should have a random mix of uppercase letters, lowercase 
letters, numbers, and punctuation symbols. The function should ask the user how strong 
they want the password to be. The user should pick from weak, strong, or very strong. 
If the user picks "weak," the function should generate a 5-character long password. 
If the user picks "strong," generate an 8-character password, and if they pick "very strong," 
generate a 12-character password.
'''

import string
import random

def generate_password ():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = string.punctuation
    list_all = list(lower + upper + symbols)
    print(list_all)
    random.shuffle(list_all)
    password = ''.join(list_all)

    print('''
                                    Welcome in password generator 
        If the You pick "weak," the function should generate a 5-character long password. 
        If the You pick "strong," generate an 8-character password, and if You pick "very strong," 
        generate a 12-character password ''')

    choice = input("What is your choice (weak/strong/very strong): ")

    if choice == 'weak':
        return password[:5]
    elif choice == 'strong':
        return password[:8]
    elif choice == 'very strong':
        return password[:12]
    else:
        f'There is no choice like {choice}'


if __name__ == '__main__':
    print(generate_password())


    


