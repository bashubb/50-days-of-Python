# 1st day:
# basic chalange: division and square root

'''
function called divide_or_square that takes one argument (a number) 
and returns the square root of the number if it is divisible by 5, 
or its remainder if it is not divisible by 5.
'''

import math

def divide_or_square(number: int):
    if number % 5 == 0:
        return math.sqrt(number)    #returns the square root of the number
    else:
        return number % 5   #returns the remainder of the number


# extra chalange: longest value

'''
function called longest_value that takes a dictionary as an argument and 
returns the first longest value of the dictionary. For example, the following 
dictionary should return "apple" as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
'''

def longest_value(dictionary: dict):
    return max(dictionary.values(), key=len)


if __name__ == "__main__":
    print(divide_or_square(10))
    print(divide_or_square(7))

    fruits = {'fruit': 'apple', 'color': 'green'}
    cars_colors = {'red': 'ferrari', 'black': 'BMW','yellow': 'Lamborghini'}
    print(longest_value(fruits))
    print(longest_value(cars_colors))




