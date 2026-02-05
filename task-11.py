'''
Task-10:
Cow & Bulls counting based on number guessing.
'''

import random

# generate a random 4 digit number
n = random.randint(1000, 9999)
number = str(n)

print(number) 
count = 0  # to count number of guesses

while True:
    cows = 0    # correct digit at correct position
    bulls = 0   # correct digit but wrong position

    # take input from user
    user_guess = input("Guess any 4 digit number: ")

    # check if input is valid
    if len(user_guess) == 4 and user_guess.isdigit():
        count += 1   

        for i in range(4):
          if number[i] == user_guess[i]: 
            cows += 1      # guessed digit in correct position 
        for i in range(4):
          if user_guess[i] in number and user_guess[i] != number[i]:
                bulls += 1     # guessed digit in wrong position 

        print(f"Cows: {cows}, Bulls: {bulls}\n")
    else:
        print("\nEnter only 4 digit number!\n")
        continue   

    if cows == 4:
        print(f"\nYou Guessed number in {count} guesses")
        break
