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
    print(f'\t\t\t\t ++++++ Welcome in {app_name} I will do my best for you ++++++\n\n')


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
            tax = int(input("please Enter value of the Vat tax in % for example - 20, 15, 50: "))
            if tax >= 100:
                print('Sorry, your tax is too high, you need to try some other value - below 100')
            else:
                break
        except ValueError:
            print('Please use numbers to enter the vaule of the tax')
   
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

    

if __name__ == '__main__':
    
    your_vat()

