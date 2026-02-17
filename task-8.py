'''
Task-8:
Matrix Multiplication
1. Take two 3x3 matrix.
2. take user inputs to fill it up.
3. Multiply them both and store it in another 3x3 matrix.
4. Display the result.
'''

# 3*3 Matrix Multiplication with User Input

# define a function for matrix multiplication
def matrix_multiplication():
  
  matrix1 = []
  matrix2 = []
  result = [[0,0,0],[0,0,0],[0,0,0]]
  
  print('\nMatrix-1') # Matrix-1
  for i in range(3):
    matrix1_array = []
    for j in range(3):
      matrix1_value = (input(f'Enter Value of [{i+1,j+1}]: ')) 
      while True:
        if matrix1_value.isdigit() == False:
          print('Invalid input, Please enter only numbers')
          matrix1_value = (input(f'Enter Value of [{i+1,j+1}]: '))
        else:    
          matrix1_array.append(int(matrix1_value))
          break
    matrix1.append(matrix1_array) # Add every row to list 

  print('\nMatrix-2') # Matrix-2
  for x in range(3):
    matrix2_array = []
    for y in range(3):
      matrix2_value = (input(f'Enter Value of [{x+1,y+1}]: '))     
      while True:
        if matrix2_value.isdigit() == False:
          print('Invalid input, Please enter only numbers')
          matrix2_value = (input(f'Enter Value of [{x+1,y+1}]: '))
        else:
          matrix2_array.append(int(matrix2_value))
          break
    matrix2.append(matrix2_array) # Add every row to list

# Multiply both matrix
  for i in range(3):
    for j in range(3):
      for k in range(3):
        result[i][j] += matrix1[i][k] * matrix2[k][j] # Multiply matrix-1 with matrix-2

# Print the multiplied matrix
  print()
  print(f'Matrix-1: {matrix1}')
  print(f'Matrix-2: {matrix2}')
  print(f'\nMatrix-1 * Matrix-2: {result}')

matrix_multiplication()