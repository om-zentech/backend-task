'''
Find Diterminent of 3*3 Matrix.
'''

# Determinent of 3*3 Matrix

m = []

# Take user input to fill the matrix
print('\nMatrix-1')
for i in range(3):
  m1 = []
  for j in range(3):
    a = int(input(f'Enter Value of [{i+1,j+1}]: '))
    m1.append(a)
  m.append(m1) # Add every row to list

ans = (m[0][0]*(m[1][1] * m[2][2] - m[1][2] * m[2][1]) 
      - m[0][1]*(m[1][0] * m[2][2] - m[1][2] * m[2][0]) 
      + m[0][2]*(m[1][0] * m[2][1] - m[1][1] * m[2][0]))  # Formula for finding Determinent

print(f'Matrix: {m}')
print(f'Determinent: {ans}')