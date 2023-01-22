#day_9th:
'''
'''


def biggest_odd(number_string: str):
    odds =[x for x in list(number_string) if int(x) % 2 != 0]
    odds.sort()
    biggest = odds[-1]

    return f'The biggest number from {number_string} converted to the list and filtered to odd numbers only {odds} is {biggest}'  

print(biggest_odd('23569'))
