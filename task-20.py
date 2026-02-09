'''
Task-20:
* * * * *
* * * *
* * *
* *
*
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(row,0,-1): # this loop prints the pattern
    print('*'*i)
  
number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0: 
    pattern(number_of_row)
else:
   print("Enter Positive number of rows only!")