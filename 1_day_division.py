'''
function called divide_or_square that takes one argument (a number) 
and returns the square root of the number if it is divisible by 5, 
or its remainder if it is not divisible by 5.
'''

import math

def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)    #returns the square root of the number
    else:
        return number % 5   #returns the remainder of the number




