# Python program to help demonstrate the basics of a stack

# Creating a stack
stack = []

# Adding an element to the stack
stack.append('item1')
stack.append('item2')
stack.append('item3')

# Output each item in the stack
print(stack)

stack.pop()
print(stack)
print(len(stack))

# See if the stack is empty or not
if len(stack) == 0:
    print(True)
else:
    print(False)  # Output: False

# Empty the stack
stack.pop()
stack.pop()
print(stack)

# See if the stack is empty or not
if len(stack) == 0:
    print(True)
else:
    print(False)  # Output: True
