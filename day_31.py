#day 31:
'''
Write a function that has one parameter and takes a list of words as an argument. 
The function returns the longest word from the list. Name the function longest_word. 
The function should return the longest word and the number of letters in that word. 
For example, if you pass ['Java', 'JavaScript', 'Python'], your function should return [10, JavaScript] 
as the longest word.
'''

def longest_word(collection: list):
    longest = max(collection, key= len)
    longest_in_list = [len(longest), longest]
    return longest_in_list

if __name__ == '__main__':

    #basic execution:
    example_list = ['Java', 'JavaScript', 'Python']
    print(longest_word(example_list))     #output :  [10, JavaScript] 