'''
Task-24:

 * * * * * * * * *
   * * * * * * *
     * * * * *
       * * *
         *
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(row,0,-1):
    print(' '*(row-i),end=' ') # this line prints spaces before pattern
    print('*'*(2*i-1),end=' ') # this line prints pattern after spaces
    print()

number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0: 
    pattern(number_of_row)
else:
   print("Enter Positive number of rows only!")