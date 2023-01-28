# basic challange:
'''
function called same_in_reverse that takes a string and checks if the string reads the same in reverse. 
If it is the same, the code should return True if not, it should return False. 
For example, ‘dad’ should return True, because it reads the same in reverse.
'''

def same_in_reverse(word: str):
    word_reverse = word[::-1]
    if word == word_reverse: 
        result = True
    else:
        result = False
    
    return f'{word} in reverse is {word_reverse}, so result is {result} '



if __name__ == '__main__':
    print(same_in_reverse('roman'))
