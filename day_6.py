# day 6th
# Basic: 
'''
function called user_name that generates a username from the user’s email. 
The code should ask the user to input an email, and the code should 
return everything before the @ sign as their user name.
'''

def user_name():
    while True:
        email = input("please type your email: ")
        if '@' in email and '.' in email:
            break
        else:
            print("that's not email ")

    name = ""
    for letter in email:
        if letter == '@':
            break
        else:
            name += letter
    
    return f"here's your {name}"


# extra challange:
# Zero both ends
'''
function called zeroed code that takes a list of numbers as an argument.
The code should zero (0) the first and last number in the list.
'''

def zeroed(collection: list):
    collection[0] = 0
    collection[-1] = 0
    return f"here's your corrected list {collection}"

if __name__ == "__main__":

    example = [2, 5, 7, 8, 9]

    print(zeroed(example))
    print(user_name())
    
