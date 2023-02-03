#day 14 
#basic challange:
'''
a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one-dimension list. 
For example [[2,4,5,6]] should return [2,4,5,6].
'''

def flat_list(collection: list):
    unnested_list = [x for x in collection[0]]
    return unnested_list

#=====================================================
# Extra challange:
'''
A school has asked you to write a program that will calculate teachers' salaries. 
The program should ask the user to enter the teacher’s name, the number of periods taught in a month, and the rate per period. 
The monthly salary is calculated by multiplying the number of periods by the monthly rate. The current monthly rate per period is $20. 
If a teacher has more than 100 periods in a month, everything above 100 is overtime. Overtime is $25 per period. 
For example, if a teacher has taught 105 periods, their gross monthly salary should be $2,125. 
Write a function called your_salary that calculates a teacher’s gross salary. The function should return the teacher’s name, 
periods taught, and gross salary. Here is how you should format your output: Teacher: John Kelly, Periods: 105 Gross salary:2,125
'''

def welcome():# say hello to the user
    print('\n\n\t\t\t This is the program wich helps you calculate teacher salary')


def enter_teacher_name():
    while True:
        name = input('\nPlease enter the name of the teacher: ')
        if name.isalpha() == False or name == ' ':
            print('\nPlease use letters to enter the name')
        else:
            break
    return name
        

def enter_number_of_periods():
    while True:
        try:
            number_of_periods = int(input('\nPlease enter number of periods taught in the month: '))  
        except ValueError:
            print('\nUse numbers to enter the value of periods ')
        break
        
    
    return number_of_periods


def enter_rate(rate=20):
    while True:
        yes_no = input(f'\n Current rate per period is {rate}\n Do you want to change it? yes/no  ')
        if yes_no.lower().startswith('n'):
            break
        else:
            while True:
                try:
                    rate = int(input('\nPlease enter new rate '))
                    break
                except ValueError:
                    print('\nUse numbers to enter the rate ')
                
    
    return rate

def calculate_final_salary(rate, period):
    if period > 100:
        final_salary = 100 * rate + ((period - 100) * (rate + 5) )
    else: 
        final_salary = period * rate
    
    return final_salary


def your_salary():
    welcome()
    name = enter_teacher_name()
    rate = enter_rate()
    num_periods = enter_number_of_periods()
    final_salary = calculate_final_salary(rate, num_periods)
    print(f'''
    Teacher: {name.title()}
    Periods: {num_periods}
    Gross salary: {final_salary}''')


if __name__ == '__main__':
    
    #execution of basic challange
    example_nested_list = [[2,4,5,6]]
    print(flat_list(example_nested_list))

    #execution of extra challange
    your_salary()

