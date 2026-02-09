'''
Task-18:
Pattern:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(1,row+1):   # this loop prints each row
    for j in range(1,i+1):   # this loop prints every elements in each row
      print(j,end=" ")
    print()

number_of_row = int(input('Enter number of row: ')) # take input of number of rows from user
if number_of_row > 0: 
    pattern(number_of_row)
else:
   print("Enter Positive number of rows only!")