'''
Task-6:
Insertion sort
Use a static list
Use insertion sort to sort this list
'''
# Insertion Sort

l = [5,12,7,3,2,15]
n = len(l)

for i in range(1,n):
  temp = l[i]
  j = i-1
  while temp < l[j] and j >= 0: # compare every element before that element
    l[j+1] = l[j] # shift element 
    j -= 1
  l[j+1] = temp # place element to it's right place
print(f'Sorted List using Insertion sort: {l}')