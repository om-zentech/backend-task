'''
Task-28:
Diamond Pattern
     * 
    *** 
   ***** 
  ******* 
 ********* 
  ******* 
   ***** 
    *** 
     * 
'''

# define a function for printing a pattern
def pattern(row):

  for i in range(1,row):
    print(' '*(row-i),end=' ') # this line prints spaces before pattern
    print('*'*(2*i-1),end=' ') # this line prints pattern after spaces
    print()

  for i in range(row,0,-1):
    print(' '*(row-i),end=' ') # this line prints spaces before pattern
    print('*'*(2*i-1),end=' ') # this line prints pattern after spaces
    print()

number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
pattern(number_of_row)

'''
time complexity: O(n^2)
because loop runs n times and in each iteration it prints 2*i-1 stars so 1+3+5+...+(2n-1) = n^2 = O(n^2)
'''