'''
Task-19:
A
B B
C C C
D D D D
E E E E E
'''

# define a function for printing a pattern
def pattern(row):
  ch = 65
  for i in range(1,row+1):   # this loop prints every elements in each row 
    for j in range(1,i+1):   # this loop prints every elements in each row
      print(chr(ch),end=" ")   # chr function convert number into character according to it's ascii value
    ch += 1  
    print()  
  
number_of_row = int(input('Enter number of row: ')) # take input of number of rows from user
if number_of_row > 0: 
    pattern(number_of_row)
else:
   print("Enter Positive number of rows only!")