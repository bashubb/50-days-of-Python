#day 38 extra:
'''
Extra Challenge: 
Find Missing Numbers list = 
[1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31] 
Write a function called missing_numbers that takes a list of s
equence of numbers and finds the missing numbers in the sequence. 
The list above should return: [4, 8, 10, 13, 16, 29, 30]
'''

def find_missing_numbers (collection: list):
    return [x for x in range(collection[0],collection[-1] + 1) if x not in collection]

if __name__ == '__main__':
    example = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31] 
    print(find_missing_numbers(example))    #output should be: [4, 8, 10, 13, 16, 29, 30]
    
