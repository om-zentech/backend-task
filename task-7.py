'''
Task-7:
Binary search
Use a static list
Use Binary search to find element asked by user
Use one of the sorting algorithm that you have developed to sort list here
'''

# Binary Search

li = [5,12,7,3,2,15,6]
n = len(li)

# Sort the list using Selection sort
def sorting(l):
  for i in range(n):
    min = i
    for j in range(i+1,n):
      if l[min] > l[j]:
        min = j
    l[min],l[i] = l[i],l[min] 
  print(f'Sorted List: {l}')

# Search element using BinarySearch
def binarySearch(l,k):
  low = 0
  high = n-1
  while low <= high:
    mid = (low + high) // 2 # Set mid at middle index of list
    if k == l[mid]: # Element found at mid index (Best Case)
      return mid
    elif k > l[mid]: # Element present in right side of mid
      low = mid+1
    else: # Element present in left side of mid 
      high = mid-1
  return -1 # Element not found
  
sorting(li)
user_input = int(input("Enter Value: ")) # User Input 
answer = binarySearch(li,user_input)

if answer != -1:
  print(f"Element {user_input} Found at index: {answer}")
else:
  print("Element not present in list")