'''
Implement Queue You script should contain three functions
1. enqueue
2. dequeue
3. peek 
User will be given choice to perform action from above three. Script should be kept running until user chooses to exit.
'''

# Queue Operations

queue = []

# Enqueue Operation
def enqueue():
  element = input("Enter element: ")
  queue.append(element)
  print(f'{element} added to queue')
  print(f'Queue: {queue}')

# Dequeue Operation
def dequeue():
  if len(queue) == 0:
    print("Queue is Empty")
  else: 
    print(f'{queue.pop(0)} removed from queue')
    print(f'Queue: {queue}')

# Peek (gives frist element of queue)
def peek():
  if len(queue) == 0:
    print("Queue is Empty")
  else:
    print(f'{queue[0]} is first element of queue')

# Choice Menu
while True:

  print("\n1.Enqueue / 2.Dequeue / 3.Peek / 4.Exit")
  ch = input("Enter Choice: ")

  if ch == '1':
    enqueue()
  elif ch == '2':
    dequeue()
  elif ch == '3':
    peek()
  elif ch == '4':
    print("Exiting..")
    break
  else:
    print("Invalid choice, try again!")