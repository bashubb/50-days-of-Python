#day 24
#basic:
'''
Write a function called average_calories that calculates the average calorie intake of a user. 
The function should ask the user to input their calorie intake for any number of days, 
and once they hit "done," it should calculate and return the average intake.
'''
import time


def average_calories():
    while True:
        try:
            calorie_intake = float(input('Please enter number of calories: '))
            number_of_days = int(input('And number of days : '))
            if calorie_intake <= 0 or number_of_days <= 0:
                print('\nValues need to be positive!')
                continue
            if isinstance(calorie_intake, float) or isinstance(number_of_days, int):
                break
        except ValueError:
            print("\nYou need to use numbers, please try once again! ")
    
    input('\nIf You are ready to calculate the average of calories please press Enter!')
    print('\nCalculate the average')
    for i in range(5):
        print('*')
        time.sleep(1)

    print(f'The Average calories per day is {calorie_intake / number_of_days}')

#extra challange:
'''
a function called nested_lists that takes any number of lists and creates 
a 2-dimensional nested list of lists. For example, if you pass the following 
lists as arguments: [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]. 
Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
'''

def nestetd_list(*collections):
    return [collection for collection in collections]

if __name__ == '__main__':

    #executing basic 
    average_calories()

    #executin extra
    first = [1, 2, 3, 5]
    second = [1, 2, 3, 4]
    third = [1, 3, 4, 5]

    print(nestetd_list(first, second, third))
    