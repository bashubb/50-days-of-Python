#day 38
#basics:
'''
function called guess_a_number. 
The function should ask a user to guess a randomly generated number. 
If the user guesses a higher number, the code should tell them that 
the guess is too high; if the user guesses a low number, the code should 
tell them that their guess is too low. The user should get a maximum of three(3) guesses.
When the user guesses right, the code should declare them a winner. 
After three wrong guesses, the code should declare them a loser.
'''
import random

def guess_a_number ():
    print("You have 3 opportunities to guess the number !")
    number_to_guess = random.randrange(1,10)
    counter = 0

    while True:
        if counter == 3:
            print('You have reach all chances - You loose ')
            break
        guess = int(input('Please guess a number in range 1 - 10: '))
        counter += 1
        if guess not in range(1,11):
            print(f'number {guess} is not in the range, please try again')
            continue
        if guess > number_to_guess:
            print('number is to high')
            continue
        elif guess < number_to_guess:
            print('number is to low!! please try again')
            continue
        else:
            print(f'Congratulations you win! {guess} is right number !')
            break
    

if __name__ == '__main__':
    guess_a_number()



