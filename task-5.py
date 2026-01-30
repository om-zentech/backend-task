'''
Task-5:
Bubble sort
Use a static list
Use bubble sort to sort this list
'''

# Bubble Sort

l = [2,5,3,10,1,6,9] # Static List
n = len(l)

for i in range(n):
  if i == n-1:
    print(f'\nSorted List Using Bubble Sort: {l}')
  else: 
    print(f'\nStep-{i+1}:') # Prints Every Steps of swapping
  for j in range(0,n-i-1):
    if l[j] > l[j+1]:
      l[j],l[j+1] = l[j+1],l[j] # Swapping Element
    print(f'{l}')