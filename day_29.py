#day29
#basic:
'''
function called middle_figure that takes two parameters, a and b. 
The two parameters are strings. The function joins the two strings and finds the middle element. 
If the combined string has a middle element, the function should return the element; otherwise, 
it should return "no middle figure." Use "make love" 
as an argument for a, and "not wars" as an argument for b. 
Your function should return "e" as the middle element. Whitespaces should be removed.
'''

def middle_figure(first_word: str, second_word: str):
    new_word = (first_word + second_word).replace(' ', '')
    if len(new_word) % 2 == 0:
        middle_index = (len(new_word) / 2) - 1 
        return new_word[middle_index]
    else:
        return 'no middle figure' 
    