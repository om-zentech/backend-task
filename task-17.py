'''
Task-17:
Pattern:
*
* *
* * *
* * * *
* * * * *
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(1,row+1):  # this loop prints the pattern
      print('*'*i)
  
number_of_row = int(input('Enter number of row: ')) # take input of number of rows from user
pattern(number_of_row)