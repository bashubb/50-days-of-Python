#day 25
#basic:
'''
function called all_the_same that takes one argument, 
a string, a list, or a tuple, and checks if all the elements are the same. 
If the elements are the same, the function should return True. If not, it should 
return False. For example, ["Mary", "Mary", "Mary"] should return True.
'''

def all_the_same(collection):
    counter = 0 
    for i in range(len(collection)):
        if collection[i] != collection[i - 1]:
            counter += 1
    if counter != 0:
        return False
    return True

if __name__ == '__main__':

    #executing basic:

    first_example = ["Mary", "Mary", "Mary"]        #True
    second_example = ("Mary", "Mary", "Natasha")    #False
    third_example = 'aaaaaaaa'                      #True
    fourth_example = 'aaaab'                        #False

    print(all_the_same(first_example))
    print(all_the_same(second_example))
    print(all_the_same(third_example))
    print(all_the_same(fourth_example))