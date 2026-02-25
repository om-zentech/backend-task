'''
Task-21:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

# define a function for printing a pattern
def pattern(row):
  for i in range(row,0,-1): # this loop prints each row
    for j in range(1,i+1):  # this loop prints every elements in each row
      print(j,end=" ")
    print()

while True:
  try:
    number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
    if number_of_row > 0:
      pattern(number_of_row)
    else:
      print("Enter Positive number of rows only!")
      continue
    break
  except ValueError:
    print("Invalid input! Please enter a positive integer.")

'''
time complexity: O(n^2)
because loop runs n times and in each iteration it prints i numbers so 1+2+3+...+n = n(n+1)/2 = O(n^2)
'''