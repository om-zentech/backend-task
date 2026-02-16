'''
Task-27:
1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7
'''

# define a function for printing a pattern
def pattern(n):
    arr = [[0] * n for i in range(n)]
    print(arr)
    
    num = 1
    left,right,top,bottom = 0,n-1,0,n-1
    
    while num <= n * n:
        # Traverse from left to right
        for i in range(left, right + 1):
            arr[top][i] = num
            num += 1
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            arr[i][right] = num
            num += 1
        right -= 1
        
        # Traverse from right to left
        for i in range(right, left - 1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1
        
        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            arr[i][left] = num
            num += 1
        left += 1
    
    # this loop prints the pattern
    for row in arr:
        print(" ".join(f"{x:2}" for x in row))

number_of_row = int(input('Enter number of row: '))  # take input of number of rows from user
if number_of_row > 0:
    pattern(number_of_row)
else:
    print("Enter Positive number of rows only!")

'''
time complexity: O(n^2)
because we need to fill n*n elements in the matrix and each element is filled once, so the time complexity is O(n^2)
'''