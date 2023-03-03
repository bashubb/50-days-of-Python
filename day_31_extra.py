#day 31
#extra:
'''function called create_user. 
This function asks the user to enter their name, age, and password. 
The function saves this information in a dictionary. 
For example, if the user enters Peter as his name, 18 as his age,
and "love" as his password, the function should save
the information as: {"name": "Peter", "age": "18", "password": "love"}
Once the information is saved, the function should print to the user, 
"User saved. Please login" The function should then ask the user to re-enter their name and password. 
If the name and password match what is saved in the dictionary, 
the function should return "Logged in successfully." 
If the name and password do not match what is saved in the dictionary, 
the function should print "Wrong password or user name, please try again". 
The function should keep running until the user enters the correct logging details.
'''


def create_user():
    name = input('Please enter your name: ')
    age = input('Please eneter your age: ')
    password = input('Please enter your password: ')

    user = {'name': name, 'age': age, 'password': password}
    print('User saved. Please log in ')

    name_check = ''
    password_check = ''

    while True:
        name_check = input('Please enter your name: ')
        password_check = input('Please eneter your password: ')
        if name_check != name or password_check != password:
            print('Wrong password or user name, please try again')
        else: 
            break

    print('Logged in successfully.')


if __name__ == '__main__':

    #execute 
    create_user()
