'''
Task-4
Selection sort
Use a static list
Use selection sort to sort this list
'''

# Selection Sort

l = [2,5,3,1,6,9] # Static List
n = len(l)

for i in range(n):
  min = i
  print(f'Step-{i+1}:\n{l}')
  for j in range(i+1,n): # Find Minimum Element from List
    if l[min] > l[j]: 
      min = j 
  print(f'Minimum Element: {l[min]}\n')
  l[min],l[i] = l[i],l[min] # Swaping with Minmum Element
  
print(f'Sorted List Using Selection Sort: {l}')