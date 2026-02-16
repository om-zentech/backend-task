'''
Task-25:
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(row):
    for j in range(row-i):
      print(" ",end='')
    number = 1
    for k in range(i+1):
      print(number,end=' ')
      number = number * (i - k) // (k + 1)
    print()
number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0:
    pattern(number_of_row)
else:
    print("Enter Positive number of rows only!")

'''
time complexity: O(n^2)
because loop runs n times and in each iteration it prints i numbers so 1+2+3+...+n = n(n+1)/2 = O(n^2)
'''