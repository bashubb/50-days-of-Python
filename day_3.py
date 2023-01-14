# 3rd day
# basic challange: register check

def register_check(collection: dict):
    number_of_students = 0
    for value in collection.values():
        if value.lower() == "yes":
            number_of_students += 1
    return number_of_students


# extra challange: 


def find_lowercase(collection: list):
    lower_case_list = [item for item in collection if item.islower()]
    return tuple(lower_case_list)

names = ["kerry", "dickson", "John", "Mary", 
         "carol", "Rose", "adam"]


register = {'Michael':'yes','John': 'no', 
            'Peter':'yes', 'Mary': 'yes'}

print(register_check(register))
print(find_lowercase(names))
