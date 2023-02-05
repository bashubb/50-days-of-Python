#day 18
#basic challange:
'''
a function called any_number that can receive any number of arguments 
(integers and floats) and return the average of those integers. 
If you pass 12, 90, 12, 34 as arguments, your function should return 37.0 as the average.
If you pass 12 and 90 your function should return 51.0 as the average. 
'''

def any_number(*numbers):
    return sum(numbers) / len(numbers)


#challange
'''
function called add_reverse. This function takes two lists as argument,
and adds each corresponding number, and reverses the outcome. For example, 
if you pass [10, 12, 34] and [12, 56, 78]. Your code should return [112, 68, 22]. 
If the two lists are not of equal length, the code should 
return a message that "the lists are not of equal lengths."
'''

def add_reverse(first: list, second: list):
    if len(first) != len(second):
        return 'the lists are not of equal lengths.'
    else:
        pairs = list(zip(first, second))
        pairs.reverse()
        return [sum(x) for x in pairs]


if __name__ == '__main__':
    
    #execution basic
    print(any_number(2,2,2,3,3,5))

    #execution challange
    first_example = [10, 12, 34]
    second_example = [12, 56, 78]
    print(add_reverse(first_example, second_example))