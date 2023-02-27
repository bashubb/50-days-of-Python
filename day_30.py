#day30
#basic:
'''
repeated_name that finds the most repeated name in the following list. 
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
'''

def repeated_name(collection: list):
    count_names = {name: collection.count(name) for name in collection}
    return max(count_names.items())


if __name__ == '__main__':
    
    # execute basic:
    example = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    print(repeated_name(example))