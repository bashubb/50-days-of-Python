#day 20
#basic
'''
Write a function called capitalize.
This function takes a string as an argument and 
capitalizes the first letter of each word. For example, 
"i like learning" becomes "I Like Learning."
'''

def capitalize(sentence: str):
    return ' '.join([x.capitalize() for x in sentence.split()])


#Extra Challenge
'''
Extra Challenge: Reversed List str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success' 
You are given a string of words. Some of the words in the string contain uppercase letters.
Write a code that will return all the words that have an uppercase letter. 
Your code should return a list of the words. Each word in the list should be reversed. 
Here is how your output should look: ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
'''
def reversed_list (sentence: str):
    list_of_upper = [word[::-1] for word in sentence.split() if any(letter.isupper() for letter in word)]
    
    return list_of_upper

if __name__ == '__main__':

    #execute basic
    example_sentence = 'i like learning'
    print(capitalize(example_sentence))

    #execute challange
    str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
    print(reversed_list(str1))