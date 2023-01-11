import math

def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5 


print(divide_or_square(10))
print(divide_or_square(12))
print(divide_or_square(13))
print(divide_or_square(15))

