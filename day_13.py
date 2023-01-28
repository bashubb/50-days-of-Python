#day 13
#Basic challange
'''
function called your_vat. The function takes no parameters. 
The function asks the user to input the price of an item and VAT (VAT should be a percentage). 
The function should return the price of the item plus VAT. If the price is 220 and the VAT is 15%, 
your code should return a VAT-inclusive price of 253. Check to see if your code can handle ValueError. 
Ensure the code runs until valid numbers are entered.
'''

def welcome(app_name): # say welcome to user
    print(f'\n\n\t\t\t\t ++++++ Welcome in {app_name} I will do my best for you ++++++\n\n')


def take_price(): # take price from the user
    while True:
        try:
            price = float(input('Please enter your price: '))
            break
        except ValueError:
            print('Please use numbers to enter the price')

    return price


def take_tax(): # take value of the price from the user
    while True:
        try:
            tax = int(input("\nplease Enter value of the Vat tax in % for example - 20, 15, 50: "))
            if tax >= 100:
                print('\nSorry, your tax is too high, you need to try some other value - below 100')
            else:
                break
        except ValueError:
            print('\nPlease use numbers to enter the vaule of the tax')
   
    tax *= 0.01
    return tax

def your_vat(): # main function of program
    welcome('your vat')
    price = take_price()
    print()
    tax = take_tax()
    result = price + (tax * price) 
    print()
    print(f'Your final price with Vat tax included is {result}')

#===================================================================================================
#Extra challange:
# it's nesessery to install emoji library
'''
function called python_snakes that takes a number as an argument
 and creates the following shape using the number’s range.
'''
import time

import emoji


def how_long_the_snake(): #takes lenght of the snake from user
    while True:
        try:
            len_of_snake = int(input('Please enter lenght of the snake: '))
            break
        except ValueError:
            print('Please use numbers to define lenght of the snake: ')

    return len_of_snake

def print_snake(number): #prints the snake

    print('loading')
    for _ in range(5):
        time.sleep(1)
        print('++')

    for i in range(1, number):
        print(i * ((2* emoji.emojize(':question:',language='alias')) + ' '))
        

def python_snakes():
    welcome('python_snake')
    print_snake(how_long_the_snake())
    
    


 


if __name__ == '__main__':
    
    your_vat()
    python_snakes()

