'''
Task-6:
Insertion sort
Use a static list
Use insertion sort to sort this list
'''
# Insertion Sort

def insertion_sort():
  static_list = [5,12,7,3,2,15]

  for i in range(1,len(static_list)):
    copy_list = static_list[i]
    j = i-1

    while j >= 0 and copy_list < static_list[j]: # compare every element before that element
      static_list[j+1] = static_list[j] # shift element 
      j -= 1

    static_list[j+1] = copy_list # place element to it's right place
  return f'Sorted List using Insertion sort: {static_list}'

print(insertion_sort())