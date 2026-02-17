'''
Find Diterminent of 3*3 Matrix.
'''

# Determinent of 3*3 Matrix


def determinant():
  matrix = []

  # Take user input to fill the matrix
  print('\nMatrix-1')
  for i in range(3):
    matrix_array = []
    for j in range(3):
      matrix_value = (input(f'Enter Value of [{i+1,j+1}]: '))

      while True:
        if matrix_value.isdigit() == False:
          print('Invalid input, Please enter only numbers')
          matrix_value = (input(f'Enter Value of [{i+1,j+1}]: '))
        else:
          break
        
      matrix_array.append(int(matrix_value))
    matrix.append(matrix_array) # Add every row to list

  ans = (matrix[0][0]*(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) 
        - matrix[0][1]*(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) 
        + matrix[0][2]*(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))  # Formula for finding Determinent

  print(f'Matrix: {matrix}')
  return f'Determinent: {ans}'

print(determinant())