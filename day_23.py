#day 23
#basic:
'''
Create a simple calculator.
The calculator should be able to perform basic math operations: 
add, subtract, divide, and multiply. The calculator should take input from users. 
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.
'''

def welcome():
    print('''
                        Hello, I'm simple calculator app! I'm going to help you with math.
                At first enter 2 numbers, then choose operation that you want to do with them. Have fun !''')


def choose_operation():
    choose =('''
                    Please choose the operation.
                    + for add
                    - for subtract
                    : or / for divide 
                    * for multiply
    ''')
    print(choose)
    while True:
        operation = input()
        if operation not in ['+', '-', ':', '/', '*']:
            print(f'You have selected wrong character, please try again{choose}')
        else:
            break
    return operation


def enter_numbers():
    print('\nIn this app you are able to do operations on 2 numbers. Please enter numbers')
    numbers = []
    for i in range(2):
        while True:
            try:
                number =  float(input())
                numbers.append(number)
                break
            except ValueError:
                print("\nPlease enter valid Value, You need to use numbers")
    return numbers


def calculate(numbers, operation):
    if operation == '+':
        return numbers[0] + numbers[1]
    elif operation == '-':
        return numbers[0] - numbers[1]
    elif operation == '*':
        return numbers[0] * numbers[1]
    elif operation == ':' or operation == '/':
        try:
            return numbers[0] / numbers[1]
        except ZeroDivisionError:
            print('You can not divide by zero')
            return 'zero_division'

        
    

def yes_no():
    while True:
        answer = input('Do you want to calculate something else? (yes/no): ')
        if answer in ('yes', 'no') :
            break
        elif answer.isalpha() == False:
            print('Please use letters')
    return answer
        


def main():
    welcome()
    answer = ' '
    while answer.lower() != 'no':
        numbers = enter_numbers()
        operation = choose_operation()
        result = calculate(numbers, operation)
        if result == 'zero_division':
            print('Please try to enter numbers and operation once again, please remember - do not divide by zero!')
            continue
        print(f'Result of {numbers[0]} {operation} {numbers[1]} is {result}')
        answer = yes_no()
    print('I hope You have fun! bye bye')
        
        
if __name__ == '__main__':
    main()



