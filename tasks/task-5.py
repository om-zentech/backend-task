'''
Task-5:
Bubble sort
Use a static list
Use bubble sort to sort this list
'''

# Bubble Sort

def bubble_sort():
  static_list = [2,5,3,10,1,6,9] # Static List

  for i in range(len(static_list)-1):

    if i == len(static_list)-1:
      print(f'\nSorted List Using Bubble Sort: {static_list}')
    else: 
      print(f'\nStep-{i+1}:') # Prints Every Steps of swapping

    for j in range(0,len(static_list)-i-1):
      if static_list[j] > static_list[j+1]:
        static_list[j],static_list[j+1] = static_list[j+1],static_list[j] # Swapping Element
      print(f'{static_list}')

print(bubble_sort())