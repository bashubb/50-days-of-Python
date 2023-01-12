def convert_add(list: list):
    converted_list = [int(item) for item in list]
    print(converted_list)
    sum = 0
    for item in converted_list:
        sum += item
    return  sum
 
def check_duplicates(collection: list):
    no_duplicates = []
    duplicates = []
    for item in collection:
        if item not in no_duplicates:
            no_duplicates.append(item)
        else:
            duplicates.append(item)
    if duplicates:
        return duplicates
    else:
        return "no duplicates."
        


if __name__ == "__main__":

    example_list = ["1", "3", "5"]
    example_list_2 = [2, '5', '12',22]

    print(convert_add(example_list))
    print(convert_add(example_list_2))

    fruits = ['apple', 'orange', 'banana', 'apple'] 
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']

    print(check_duplicates(fruits))
    print(check_duplicates(names))






