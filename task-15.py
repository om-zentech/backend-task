'''
Task-15:
Find the factors of a number opimize it as much as you can
'''

import math

# define a function for finding factors of a number
def factors_of_number(number):
  list_of_factors = []
  for i in range(1,int(math.sqrt(number)+1)): # 
    if number % i == 0:
      list_of_factors.append(i) # add factor to list if number is divisible by i
      list_of_factors.append(number // i)
  return list_of_factors

# take input of a number from user
while True:
  try:
    number_input = int(input('Enter Number: '))
    print(sorted(set(factors_of_number(number_input)))) # prints factors of number in sorted order & remove duplicates
    break
  except ValueError:
    print("Invalid Input try again!\n")