#day_9th:
'''
a function called biggest_odd that takes a string of 
numbers and returns the biggest odd number in the list.
'''


def biggest_odd(number_string: str):
    odds =[x for x in list(number_string) if int(x) % 2 != 0]
    odds.sort()
    biggest = odds[-1]

    return f'The biggest number from {number_string} converted to the list and filtered to odd numbers only {odds} is {biggest}'  

#Extra challange:
'''
function called zeros_last. This function takes a list as an argument. 
If a list has zeros (0), it will move them to the end of the list and maintain 
the order of the other numbers in the list. If there are no zeros in the list, 
the function should return the original list sorted in ascending order.
'''

def zeros_last(collection: list):
    counter_of_zero = collection.count(0)
    if 0 in collection:
        for number in collection:
            if number == 0:
                collection.remove(number)
        sorted_collection = sorted(collection)
        for number in range(counter_of_zero):
            sorted_collection.append(0)
        return sorted_collection
    else:
        collection.sort()
        return collection

if __name__ == '__main__':

    print(biggest_odd('23569'))

    example_1 = [1, 4, 6, 0, 7, 0, 9]
    example_2 = [2, 1, 4, 7, 6]

    print(zeros_last(example_1))
    print(zeros_last(example_2))
