#day 27
#basic:
'''
function called unique_numbers that takes a list of numbers as an argument.
Your function is going to find all the unique numbers in the list. 
It will then sum up the unique numbers. 
You will calculate the difference between the sum of 
all the numbers in the original list and the sum of the unique
numbers in the list. If the difference is an even number, 
your function should return the original list. If the difference is an odd number,
your function should return a list with unique numbers only. 
For example [1, 2, 4, 5, 6, 7, 8, 8] should return [1, 2, 4, 5, 6, 7, 8, 8].
'''

def unique_nubers(collection: list):
    all_numbers = collection[:]
    unique = list(set(collection))
    difference = sum(all_numbers) - sum(unique)
    if difference % 2 == 0:
        return all_numbers
    return unique


#extra:
'''
function called difference that takes two lists as arguments.
This function should return all the elements that are in list 
a but not in list b and all the elements in list b but not in list a. 
For example: list1 = [1, 2, 4, 5, 6] list2 = [1, 2, 5, 7, 9] should return: [4, 6, 7, 9] 
Use list comprehension in your function
'''

def difference(list1: list, list2: list):
    first_difference = set(list1).difference(list2)
    second_difference = set(list2).difference(list1)
    return list(first_difference) + list(second_difference)


if __name__ == '__main__':
    
    #basic execution:
    first_example = [1, 2, 4, 5, 6, 7, 8, 8]
    print(unique_nubers(first_example))  #output : [1, 2, 4, 5, 6, 7, 8, 8]

    #extra execution
    list1 = [1, 2, 4, 5, 6] 
    list2 = [1, 2, 5, 7, 9]
    print(difference(list1, list2))     #output :  [4, 6, 7, 9] 

