'''
Implement Circular Queue You script should contain four functions
Front: Get the front item from queue.
Rear: Get the last item from queue.
enqueue(value)
dequeue()
User will be given choice to perform action from above four. Script should be kept running until user chooses to exit.
'''

# Circular Queue Operations

queue_size = int(input("Enter size of queue: "))
input_queue = [None] * queue_size
queue_front = 0
queue_rear = 0
queue_n = 0

# Enqueue Operation on Circular Queue
def c_enqueue(queue, front, rear, n, size, value):
    if n == size:
        print("Circular Queue Overflow!")
    else:
        queue[rear] = value
        rear = (rear + 1) % size
        n += 1
        print(f'{value} added to circular queue')
    print(f'Queue: {queue}')
    return rear, n  # Return updated values to the main loop

# Dequeue Operation on Circular Queue
def c_dequeue(queue, front, rear, n, size):
    if n == 0:
        print("Circular queue Underflow!")
    else:
        value = queue[front]
        queue[front] = None
        front = (front + 1) % size
        n -= 1
        print(f'{value} removed from circular queue')
        print(f'Queue: {queue}')
    return front, n  # Return updated values to the main loop

# Get Front (It returns front value from circular queue)
def getFront(queue, front, rear, n):
    if n == 0:
        print("Circular Queue is Empty")
    else:
        print(f'Front is: {queue[front]}')

# Get Rear (It returns rear value from circular queue)
def getRear(queue, front, rear, n, size):
    if n == 0:
        print("Circular Queue is Empty")
    else:
        rear_index = (rear - 1 + size) % size
        print(f'Rear is: {queue[rear_index]}')

# Choice Menu
while True:
    print("\n1.Enqueue / 2.Dequeue / 3.getFront / 4.getRear / 5.exit")
    ch = input("Enter choice: ")

    if ch == '1':
        value = input("Enter value: ")
        # Update the variables with the return values
        queue_rear, queue_n = c_enqueue(input_queue, queue_front, queue_rear, queue_n, queue_size, value)
    elif ch == '2':
        # Update the variables with the return values
        queue_front, queue_n = c_dequeue(input_queue, queue_front, queue_rear, queue_n, queue_size)
    elif ch == '3':
        getFront(input_queue, queue_front, queue_rear, queue_n)
    elif ch == '4':
        getRear(input_queue, queue_front, queue_rear, queue_n, queue_size)
    elif ch == '5':
        print("Exiting..")
        break
    else:
        print("Invalid Choice, try again!")