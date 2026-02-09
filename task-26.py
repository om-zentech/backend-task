'''
Task-26:
1
2 3
4 5 6
7 8 9 10
'''

# define a function for printing a pattern
def pattern(row):
  n = 1
  for i in range(1,row+1): # this loop prints each row
    for j in range(i):     # this loop prints every elements in each row
      print(n,end=" ")
      n += 1
    print()

number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0: 
    pattern(number_of_row)
else:
   print("Enter Positive number of rows only!")