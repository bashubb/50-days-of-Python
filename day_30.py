#day30
#basic:
'''
repeated_name that finds the most repeated name in the following list. 
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
'''

def repeated_name(collection: list):
    count_names = {name: collection.count(name) for name in collection}
    return max(count_names.items())


#extra:
'''
You work for a local school in your area. 
The school has a list of names of students saved in a list. 
The school has asked you to write a program that takes a list of names and sorts them alphabetically.
The names should be sorted by last names. 
Here is a list of names: ["Beyoncé Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise”] 
Your code should not just sort them alphabetically; it should also switch the names
(the last name must be the first). 
Here is how your code output should look: 
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyoncé', 'Perry Katie'] 
Write a function called sorted_names
'''

def sorted_name(collection: list):
    seperated_names = [name.split() for name in collection]
    switched_names = [' '.join(item[::-1]) for item in seperated_names]
    sorted_names = sorted(switched_names)
    return  sorted_names


if __name__ == '__main__':
    
    # execute basic:
    example = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    print(repeated_name(example))   #output : ('Peter', 3)

    #execute extra:
    example_names = ["Beyoncé Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
    print(sorted_name(example_names))   #output : ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyoncé', 'Perry Katie']

