'''
Task-8:
Matrix Multiplication
1. Take two 3x3 matrix.
2. take user inputs to fill it up.
3. Multiply them both and store it in another 3x3 matrix.
4. Display the result.
'''

# 3*3 Matrix Multiplication with User Input

matrix1 = []
matrix2 = []
result = [[0,0,0],[0,0,0],[0,0,0]]

# Take user input to fill the matrix
def matrix_input():
  print('\nMatrix-1') # Matrix-1
  for i in range(3):
    m1 = []
    for j in range(3):
      a = int(input(f'Enter Value of [{i+1,j+1}]: '))     
      m1.append(a)
    matrix1.append(m1) # Add every row to list 

  print('\nMatrix-2') # Matrix-2
  for x in range(3):
    m2 = []
    for y in range(3):
      b = int(input(f'Enter Value of [{x+1,y+1}]: '))     
      m2.append(b)
    matrix2.append(m2) # Add every row to list

# Multiply both matrix
def matrix_multiplication():
  for i in range(3):
    for j in range(3):
      for k in range(3):
        result[i][j] += matrix1[i][k] * matrix2[k][j] # Multiply matrix-1 with matrix-2

# Print the multiplied matrix
def matrix_result():
  print()
  print(f'Matrix-1: {matrix1}')
  print(f'Matrix-2: {matrix2}')
  print(f'\nMatrix-1 * Matrix-2: {result}')


matrix_input()
matrix_multiplication()
matrix_result()