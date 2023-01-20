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

#Extra challange:
'''
'''

def dictonary_of_names(collection: list):
    dictonary_of_names = {}
    for name in collection:
        if name.startswith('S') and name not in dictonary_of_names:
            dictonary_of_names.update({name: 1})
        elif name.startswith('S') and name in dictonary_of_names:
            dictonary_of_names[name] += 1
    return dictonary_of_names    


if __name__ == '__main__':
    
    names = ["Joseph","Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera", "Patel", "Sera"]


    print(dictonary_of_names(names))



    print(string_range(7))
