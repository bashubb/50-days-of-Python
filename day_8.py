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

if __name__ == '__main__':
    example = [1, 2, 4, 6]
    print(odd_even(example))