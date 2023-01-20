# 3rd day
# basic challange: register check
'''
function called register_check that checks how many students are in school. 
The function takes a dictionary as a parameter. If the student is in school, 
the dictionary says "yes." If the student is not in school, the dictionary says "no."
'''

def register_check(collection: dict):
    number_of_students = 0
    for value in collection.values():
        if value.lower() == "yes":
            number_of_students += 1
    return number_of_students


# extra challange: 
'''
Task is to write a code that will return a tuple of all the names in the list
that have only lowercase letters. Your tuple should have names sorted alphabetically 
in descending order. 
'''


def find_lowercase(collection: list):
    lower_case_list = [item for item in collection if item.islower()]
    lower_case_list.sort(reverse= True)
    return tuple(lower_case_list)



if __name__ == "__main__":
    names = ["kerry", "dickson", "John", "Mary", 
            "carol", "Rose", "adam"]
    register = {'Michael':'yes','John': 'no', 
                'Peter':'yes', 'Mary': 'yes'}

    print(register_check(register))
    print(find_lowercase(names))
