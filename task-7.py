'''
Task-7:
Binary search
Use a static list
Use Binary search to find element asked by user
Use one of the sorting algorithm that you have developed to sort list here
'''

# Binary Search

static_list = [5,12,7,3,2,15,6]

# Search element using BinarySearch
def binarySearch(l,k):
  low = 0
  high = len(l)-1

  # Sort the list using Selection sort
  for i in range(len(l)):
    min_value = i
    for j in range(i+1,len(l)):
      if l[min_value] > l[j]:
        min_value = j
    l[min_value],l[i] = l[i],l[min_value] 
  print(f'Sorted List: {l}')

  while low <= high:
    mid = (low + high) // 2 # Set mid at middle index of list
    if k == l[mid]: # Element found at mid index (Best Case)
      return mid
    elif k > l[mid]: # Element present in right side of mid
      low = mid+1
    else: # Element present in left side of mid 
      high = mid-1
  return -1 # Element not found
  
while True:
  try:
    user_input = int(input("Enter Value to search: "))
  except ValueError:
    print("Invalid input. Please enter an integer.")
    continue

  answer = binarySearch(static_list,user_input)
  if answer != -1:
    print(f"Element {user_input} Found at index: {answer}")
    break
  else:
    print("Element not present in list")
    break