#day 21
#basic:
'''
function called make_tuples that takes two equal lists and combines them into a list of tuples. 
For example, if list a is [1,2,3,4] and list b is [5,6,7,8], 
your function should return [(1,5), (2,6), (3,7), (4,8)].
'''

def make_tuples(first: list, second: list):
    return list(zip(first, second))


#extra challange
'''
function called even_or_average that asks a user to input five numbers.
Once the user is done, the code should return the largest even number in the inputted numbers.
If there is no even number in the list, the code should return the average of all the five numbers.
'''

def even_or_average():
    numbers = [int(input()) for x in range(5)]
    return numbers


if __name__ == '__main__':

    #execution basic
    a = [1,2,3,4]
    b = [5,6,7,8]

    print(make_tuples(a, b))
    print(even_or_average())
