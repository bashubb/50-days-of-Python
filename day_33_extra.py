#extra:
'''
You want to implement a code that will search for a number in a range. 
You have a decision to make as to whether to store the number in a set or a list. 
Your decision will be based on time. You have to pick a data type that executes faster. 
You have a range, and you can either store it in a set or a list, depending on which one executes 
faster when you are searching for a number in the range. 
See below: a = range(10000000) x = set(a) y = list(a) 
Let’s say you are looking for the number 9999999 in the range above. 
Search for this number in the list "x" and the set "y." Your challenge is to find which code executes faster.
You will select the one that executes the fastest between lists and sets. Run the two searches and time them .
'''
import datetime

def search(collection, number_to_find):
    if collection is type(list):
        start = datetime.datetime.now()
        if number_to_find in collection:
            collection.index(number_to_find)
            end = datetime.datetime.now()
    else:
        start = datetime.datetime.now()
        if number_to_find in collection:
            for item in collection:
                if item == number_to_find:
                    end = datetime.datetime.now()
                    break
                    
    time_of_search = end - start
    return time_of_search
    

def which_data_faster(range_of_numbers, number_to_find):
    numbers = range(range_of_numbers)
    list_collection = list(numbers)
    set_collection = set(numbers)

    list_time = search(list_collection, number_to_find)
    set_time = search(set_collection, number_to_find)
   

    if set_time < list_time:
        fastest = f"set is fastest, it was {set_time} and list time was {list_time}" 
    else:
        fastest = f"list is fastest, it was {list_time} and set time was {set_time}"

    return fastest


if __name__ == '__main__':

    #execute:
    print(which_data_faster(5000, 23))
    print(which_data_faster(10000000, 5433243))
    print(which_data_faster(50231454100, 22345553))
