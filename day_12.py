# day 12
# Basic challange
'''
function called count_dots. This function takes a string separated by dots as a
 parameter and counts how many dots are in the string. For example, "h.e.l.p." 
 should return 4 dots, and "he.lp." should return 2 dots.
'''
def count_dots(text: str):
    return text.count('.')

#Extra challange
'''
function called age_in_minutes that tells a user how old they are in minutes. 
Your code should ask the user to enter their year of birth, 
and it should return their age in minutes (by subtracting their year of birth to the current year). 
Here are things to look out for: 
The user can only input a 4-digit year of birth. For example, 1930 is a valid year.
However, entering any number longer or shorter than 4 digits long should render the input invalid.
Notify the user that they must enter a four-digit number.  
If a user enters a year before 1900, your code should tell the user that the input is invalid. 
If the user enters the year after the current year, the code should tell the user to input a valid year.  
The code should run until the user inputs a valid year. Your function should return the user's age in minutes. 
For example, if someone enters 1930 as their year of birth, your function should return: You are 48,355,200 minutes old.
'''
from datetime import datetime



def welcome():
    print(''' 
                            I would like to show you 'age in minutes' app ! 
                All you have to do is enter year of birth and You'll know how old are You in minutes ''')


def enter_birth_date():
    while True:
        birth_date = input('''
                        Please enter your year of birth 
                (Please notice that format of year is 4 digits, 
                year before 1900 or after curent year is invalid):  ''')
        if len(birth_date) == 4 and int(birth_date) > 1900 and int(birth_date) < datetime.now().year :
            break
        elif birth_date.isnumeric() == False:
            print('\nPlease use numbers')
        else:
            print('\nYour date format is invalid !! please try again')
    
    return int(birth_date)
        

def age_in_minutes():
    #main
    welcome()
    current_year = datetime.now().year 
    result = (current_year -  enter_birth_date()) * 525948
    print(f'\n\t\tYour age is {result} minutes')



if __name__ == '__main__':

    #execute basic
    example = "h.e.l.p."
    print(count_dots(example))
    
    #execute challange
    age_in_minutes()