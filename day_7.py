#day 7th
#basic challange:
'''
function called string_range that takes a single number and returns a string of its range. 
The string characters should be separated by dots(.).
'''

def string_range(number: list):
    range_list = [str(x) for x in range(number)]
    string_range = '.'.join(range_list)
    return string_range + '.'

if __name__ == '__main__':

    print(string_range(7))
