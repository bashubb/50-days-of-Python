#day 34:
'''
In this challenge, copy the text below and save it as a CSV file. 
Save it in the same folder as your Python file. Save it as python.csv. 
Write a function called just_digits that reads the text from the CSV file and
returns only digit elements from the file. Your function should return 1991, 2, 200, 3, 
2008 as a list of strings. 
“Python was released in 1991 for the first time. Python 2 was released in 2000 and introduced new features, 
such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). 
Python 3 was released in 2008 and was a major revision of the language that is not completely backward-compatible.”
'''
import csv

def just_digits(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_of_digits = []
        for row in csv_reader:
            list_of_words = row[0].split()
            for item in list_of_words:
                if item.isdigit():
                    list_of_digits.append(item)
    return list_of_digits
        

if __name__ == '__main__':

    file = 'python.csv'
    #basic execution:
    print(just_digits(file))