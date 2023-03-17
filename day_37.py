#day 37
#basic:
'''
a function called count_the_vowels. 
The function takes one argument, a string, and returns the number of vowels in the string. 
For example, "hello" should return two (2) vowels. If a vowel appears in a string more than once,
it should be counted as one. For example, "saas" should return one(1) vowel. 
Your code should count lowercase and uppercase vowels.
'''

def count_the_vowels (sentence: str):
    counter = 0
    vowels = 'aeiou'
    for letter in set(list(sentence)):
        if letter in vowels:
            counter += 1
    return counter

if __name__ == '__main__':
    #execute basic
    example_1 = 'hello'
    example_2 = 'saas'

    print(count_the_vowels(example_1))  #output: 2
    print(count_the_vowels(example_2))  #output: 1
