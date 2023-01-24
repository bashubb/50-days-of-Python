# day 12
# Basic challange
'''
function called count_dots. This function takes a string separated by dots as a
 parameter and counts how many dots are in the string. For example, "h.e.l.p." 
 should return 4 dots, and "he.lp." should return 2 dots.
'''
def count_dots(text: str):
    return text.count('.')

if __name__ == '__main__':

    example = "h.e.l.p."
    print(count_dots(example))