'''
Implement Circular Queue You script should contain four functions
Front: Get the front item from queue.
Rear: Get the last item from queue.
enqueue(value)
dequeue() 
User will be given choice to perform action from above four. Script should be kept running until user chooses to exit.
'''

#Circular Queue Operations

size = int(input("Enter size of queue: "))
queue = [None]*size
front = 0
rear = 0
n = 0

# Enqueue Operation on Circular Queue
def c_enqueue(value):
  global rear,n
  if front == rear and n == size:
    print("Circular Queue Overflow!")
  else:
    queue[rear] = value
    rear = (rear+1) % size
    n += 1
    print(f'{value} added to circular queue2')
  print(f'Queue: {queue}')

# Dequeue Operation on Circular Queue
def c_dequeue():
  global front,n
  if front == rear and n == 0:
    print("Circular queue Underflow!")
  else:
    value = queue[front]
    queue[front] = None
    front = (front+1) % size
    n -= 1
    print(f'{value} removed from circular queue')
    print(f'Queue: {queue}')

# Get Front (It returns front value from circular queue)
def getFront():
  print(f'Front is: {queue[front]}')

# Get Raer (It returns raer value from circular queue)
def getRear():
  print(f'Rear is: {queue[rear]}')

# Choice Menu
while True:
  
  print("\n1.Enqueue / 2.Dequeue / 3.getFront / 4.getRear / 5.exit")
  ch = input("Enter choice: ")

  if ch == '1':
    value = input("Enter value: ")
    c_enqueue(value)
  elif ch == '2':
    c_dequeue()
  elif ch == '3':
    getFront()
  elif ch == '4':
    getRear()
  elif ch == '5':
    print("Exiting..")
    break
  else:
    print("Invalid Choice, Try again!")