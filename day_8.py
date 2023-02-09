#day 8th:
#Basic Challange:
'''
function called odd_even that has one parameter and takes a list of numbers as an argument. 
The function returns the difference between the largest even number in the list and the smallest odd number in the list.
'''

def odd_even(collection: list):
    even = [x for x in collection if x % 2 == 0]
    odd = [x for x in collection if x % 2 != 0]
    even.sort()
    odd.sort()
    difference = even[-1] - odd[0]
    return difference

#Extra Challange:
'''
function called prime_numbers. This function asks the user to enter a number 
(an integer) as an argument and returns a list of all the prime numbers within its range. 
For example, if the user enters 10, your code should return [2, 3, 5, 7] as prime numbers. 
'''

def prime_numbers():
    range_for_prime = int(input('This program will find prime numbers from 0 to number You will enter. Please enter a number: '))
    primes_only = []
    for number in range(range_for_prime):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
                else:
                    primes_only.append(number)
                    break
    
    return primes_only
    


if __name__ == '__main__':
    
    example = [1, 2, 4, 6]
    print(odd_even(example))
    print(prime_numbers())