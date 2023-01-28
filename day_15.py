# basic challange:
'''
function called same_in_reverse that takes a string and checks if the string reads the same in reverse. 
If it is the same, the code should return True if not, it should return False. 
For example, ‘dad’ should return True, because it reads the same in reverse.
'''

def same_in_reverse(word: str):
    word_reverse = word[::-1]
    if word == word_reverse: 
        result = True
    else:
        result = False
    
    return f'"{word}" in reverse is "{word_reverse}", so result is {result} '

# extra challange:
'''
function called your_age. 
This function asks a student to enter their name, a
nd then it returns their age. For example, if a user enters Peter as their name, 
your function should return, "Hi, Peter, you are 27 years old." This function reads data from the database 
(dictionary below). If the name is not in the dictionary, your code should tell the user 
that their name is not in the dictionary and ask them for their age. 
Your code should then add the name and age to the dictionary of names_age below. 
Once added, your code should return to the user, "Hi, (added name), you are (added age) years old." 
Remember to convert the input from the user to lowercase letters. names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
'''


def welcome(): # say welcome to the user
    print('''
                        Welcome in program "Your age". 
    When you will enter your name, I will tell how old You are, if you are in my data base. 
                If you are not, I will ask you about your age.''')
    

def enter_name(): # asks user for name
    while True:
        name = input("\nPlease enter your name: ")
        if not name.isalpha():
            print('\nPlease use letters to enter your name: ')
        else:
            break
    return name.lower()


def check_if_exists(name, data):
    if name in data:
        return True
    return False


def how_old(): # asks user for age
    while True:
        try:
            age = int(input("\nHow old are you: "))
            if age < 1:
                print('\nYou are too young :)')
                print('\ntry again')
            else:
                break
        except ValueError:
            print('\nTo Enter your age use numbers please')
    return age


def your_age(data): #main function of program
    welcome()
    name = enter_name()
    if check_if_exists(name, data):
        print('\n You are in my data base')
        print(f'\nHi, {name.title()}, You are {data[name]} years old.')
    else:
        print('\nYou are not in my data base ')
        data[name] = how_old()
        print(f'Hi, {name.title()}, you are {data[name]}  years old.')

    

if __name__ == '__main__':
    #execute of basic challange
    print(same_in_reverse('roman'))
    
    # execute extra challange
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    your_age(names_age)

