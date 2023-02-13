#day 23
#extra challange:
'''
s = "love live and laugh"

Write a function called multiply_words that takes a string as an argument 
and multiplies the length of each word in the string by the length of other 
words in the string. For example, the string above should return 240: 
love (4), live (4), and (3), laugh (5). However, your function should only 
multiply words with all lowercase letters. If a word has one uppercase letter,
it should be ignored. For example, the following string: s = "Hate war love Peace" 
should return 12 – war (3) love (4). Hate and Peace will be ignored because they have 
at least one uppercase letter.
'''

def multiply_words(sentence: str):
    list_of_words = sentence.split()
    list_of_lenght = []
    for word in list_of_words:
        if word.islower():
            list_of_lenght.append(len(word))
    
    sum = 1
    for i in list_of_lenght:
        sum *= i
    
    return sum

if __name__ == '__main__':

    #execute 
    example1 = "love live and laugh"
    example2 = "Hate war love Peace" 

    print(multiply_words(example1))
    print(multiply_words(example2))


