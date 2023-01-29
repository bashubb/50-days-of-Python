#day 16
# basic challange:
'''
function called sum_list with one parameter that takes a nested list of integers
as an argument and returns the sum of the integers. For example, 
if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument, your function should return a sum of 33.
'''

def sum_list(collection: list):
    total = 0 
    for element in collection:
        for number in element:
            total += number
    return total


# Extra challange:
'''
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers 
from the nested list above: 34, 67, 78. Your output should be another list: [34, 67, 78]. 
The list output should not have duplicates.
'''

def unpack(collection: list):
    no_duplicates = []
    for element in collection:
        for number in element:
            if number not in no_duplicates:
                no_duplicates.append(number) 
    return no_duplicates


if __name__ == '__main__':

    # execution basic challange:
    exaple_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
    print(sum_list(exaple_list))

    #execution extra challange 
    nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    print(unpack(nested_list))