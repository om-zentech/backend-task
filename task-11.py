'''
Task-10:
Cow & Bulls counting based on number guessing.
'''

import random

def cows_and_bulls():

    # generate a random 4 digit number
    num = random.randint(1000, 9999)
    number = str(num)

    print(number) 
    count = 0  # to count number of guesses

    while True:
        cows = 0    # correct digit at correct position
        bulls = 0   # correct digit but wrong position

        # take input from user
        user_guess = input("Guess any 4 digit number: ")

        # check if input is valid
        if user_guess.isdigit() and len(user_guess) == 4:
            count += 1   

            for i in range(4):
                if number[i] == user_guess[i]: 
                    cows += 1      # guessed digit in correct position 
            for i in range(4):
                if number.count(user_guess[i]) >= user_guess.count(user_guess[i]) and user_guess[i] in number and user_guess[i] != number[i]:
                    bulls += 1     # guessed digit in wrong position 

            print(f"Cows: {cows}, Bulls: {bulls}\n")
        else:
            print("\nEnter only 4 digit number!\n")
            continue   

        if cows == 4:
            print(f"\nYou Guessed number in {count} guesses")
            break

cows_and_bulls()