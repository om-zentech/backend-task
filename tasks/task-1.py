'''
Task-1:
Implement Stack
Your script should contain three functions
1. push
2. pop
3. peep
User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.
'''

# Stack Operations

stack = []

# Push Operation
def push():
    element = input("Enter Value: ")
    stack.append(element)
    print(f"{element} Push to stack")
    print(f"Stack: {stack}")

# Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        element = stack.pop()
        print(f"{element} Popped from stack")
        print(f"Stack: {stack}")

# Peep Operation
def peep():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print(f"Top Element: {stack[-1]}")

# Choice Menu
while True:
    print("\nSelect Operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peep")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peep()
    elif choice == '4':
        print("Exiting..")
        break
    else:
        print("Invalid Choice! Try Again")