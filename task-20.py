'''
Task-20:
* * * * *
* * * *
* * *
* *
*
'''

# define a function for printing a pattern
def pattern():
  number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
  if number_of_row > 0: 
    for i in range(number_of_row,0,-1): # this loop prints the pattern
      print('*'*i)
  else:
   print("Enter Positive number of rows only!")
  
  
pattern()

'''
time complexity: O(n^2)
because loop runs n times and in each iteration it prints i stars so 1+2+3+...+n = n(n+1)/2 = O(n^2)
'''