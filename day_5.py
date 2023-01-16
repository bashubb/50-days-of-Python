# day 5th:
# Basic challange:
'''
function called my_discount. The function takes no arguments but asks
the user to input the price and the discount (percentage) of the product. 
Once the user inputs the price and discount, it calculates the price after the discount.
'''


def welcome(name_of_app):
    print(f"\t\t\t Hello and welcome in app {name_of_app}") #prints a welcome to the user


def take_price():     # takes input, and checks if its valid
    while True:
        try:
            give_the_price = float(input('Please type a price: '))
            break
        except ValueError:
            print('To give me the price use numbers, please :)')
            print()

    return give_the_price

def take_discount():     # takes input, and checks if its valid
    while True:
        try:
            give_the_discount = int(input('Please type a discount (example 10, 20, 35):  '))
            if give_the_discount >= 100:
                print("Discount can't be equal 100 % or more ;) Please try again")
            else:
                break
        except ValueError:
            print('To give me the price use numbers, please :)')
    
    discount = give_the_discount * 0.01      
    return discount

def my_discount():  #the main function of my discount app
    welcome('discount app')
    price = take_price()
    discount  = take_discount()
    result = price * ( 1 - discount)

    return f'Your final price is {result}'


# ===============================================================
# Extra chalange:
# tuple of student sex
'''
count how many males and females are in the list.
'''

def check_sex(collection: list):
    welcome('check if male or female')
    female = 0
    for item in collection:
        if item.lower() == 'female':
            female += 1
    male = len(collection) - female

    return [('Male', male), ('female', female)]


if __name__ == '__main__' :
    print(my_discount())

    print('================================')
    input('To start second app press Enter')
    print('================================')

    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
    print(check_sex(students))

