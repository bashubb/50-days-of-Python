# day 32 extra:
'''
Extra Challenge: Valid Email emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com'] 
Write a function called email_validator that takes a list of emails and checks if the emails are valid. 
Only valid emails are returned by the function. A valid email address will have the following: 
the @ symbol (if the @ sign is at the beginning of the name, the email is invalid). 
If there is more than one @ sign, the email is invalid. 
All valid emails must end with a dot com (.com); otherwise, 
the email is invalid. For example, the list of emails above should output 
the following as valid emails: ['ben@mail.com', 'kenny@gmail.com']
If no emails in the list are valid, the function should return "all emails are invalid."
'''

def email_validator(collection: list):
    output = []
    for email in collection:
        valid = True
        if "@" == email[0] or email.count('@') > 1 or email[-4:] != '.com':
            valid = False
        if valid == True:
            output.append(email) 
    return output
    
        
if __name__ == '__main__':

    #execution:
    example_list = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
    print(email_validator(example_list)) # output: ['ben@mail.com', 'kenny@gmail.com']