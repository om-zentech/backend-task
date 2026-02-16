'''
Task-23:
      1 
    2 3 2 
  3 4 5 4 3 
4 5 6 7 6 5 4 
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(1,row+1):
    print('  '*(row-i),end='') # this line prints spaces before pattern
    for j in range(i,2*i):
      print(j,end=' ')
    for k in range(2*i-2, i-1, -1):
      print(k,end=' ')
    print()

number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0:
    pattern(number_of_row)
else:
    print("Enter Positive number of rows only!")

'''
time complexity: O(n^2)
because loop runs n times and in each iteration it prints 2*i-2 numbers so 0+2+4+...+(2n-2) = n(n-1) = O(n^2)
'''