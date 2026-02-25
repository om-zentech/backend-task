'''
Task-4
Selection sort
Use a static list
Use selection sort to sort this list
'''

# Selection Sort

def selection_sort():
  static_list = [2,5,3,1,6,9] # Static List

  for i in range(len(static_list)-1):

    min_value = i
    print(f'Step-{i+1}:\n{static_list}')

    for j in range(i+1,len(static_list)): # Find Minimum Element from List
      if static_list[min_value] > static_list[j]: 
        min_value = j 

    print(f'Minimum Element: {static_list[min_value]}\n')
    static_list[min_value],static_list[i] = static_list[i],static_list[min_value] # Swaping with Minmum Element
    
  return f'Sorted List Using Selection Sort: {static_list}'

print(selection_sort())