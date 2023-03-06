#day 33
#basic:
'''
a function called inter_section that takes two lists and finds the intersection 
(the elements that are present in both lists). The function should return a tuple 
of intersections. Use list comprehension in your solution. Use the lists below. 
Your function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85] 
list2 = [42, 30, 80, 65, 68, 88, 95] 
'''

def inter_section(collection_1: list, collection_2: list):
    return tuple([x for x in set(collection_1).intersection(set(collection_2))])

if __name__ == '__main__':

    # execute basic:
    list1 = [20, 30, 60, 65, 75, 80, 85] 
    list2 = [42, 30, 80, 65, 68, 88, 95] 
    print(inter_section(list1, list2)) # output : (30, 65, 80)  
     
