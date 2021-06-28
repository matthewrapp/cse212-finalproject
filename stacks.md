# Stacks

## Introduction

### **What is a Stack?**

- A Stack in a type of Data Structure that follows a particular order in how operations are performed.
- LIFO - Last In, First Out
- Add to the back, but pull from the back as well.
- An example of a stack, in a real-world scenario, think of a stack of plates. When you put plates away, you put them on top of the other clean plates that were already there, but when you need a plate to use, you pull from the top.
- ![Stack Representaion](images/stack-rep-1.jpeg)

### **Purpose for a Stack in Real World Application**

- Stacks could be used to store Web Browswer History.
- Undo/Redo within applicaitons
- Good for remembering where you've been.
  <br><br>

## Using A Stack in Python

A Stack in Python is represented using a list.

### **Operations used within a Python Stack**

- .append()
  - This built-in Python function is used to add a data element to the stack.
  - In Big O Notation, this operation takes O(1) time.
- .pop()
  - This built-in Python function is used to pop off the latest element that was added to the stack.
  - In Big O Notation, this operation takes O(1) time.
- .len()
  - This built-in Python function is used to get the length of the stack/list.
  - Also good to use to check if the stack is empty or not.
  - In Big O Notation, this operation takes O(1) time.

<hr style='border-width: .5px; padding-top: 10px; padding-bottom: 5px;' />

## Code Example of a Stack in Python

```python
# Python code to help demonstrate the basics of a stack

# Creating a stack
stack = []

# Adding an element to the stack
stack.append('item1')
stack.append('item2')
stack.append('item3')

# Output each item in the stack
print(stack) # Output: ['item1', 'item2', 'item3']

# Pop the last inserted element out of the stack
stack.pop()
print(stack) # Output: ['item1', 'item2']

# Get the length of the stack
print(len(stack)) # Output: 2

# See if the stack is empty or not
if len(stack) == 0:
    print(True)
else:
    print(False)  # Output: False

# Empty the stack
stack.pop()
stack.pop()
print(stack) # Output: []

# See if the stack is empty or not
if len(stack) == 0:
    print(True)
else:
    print(False)  # Output: True
```

## Resources

- https://www.geeksforgeeks.org/stack-data-structure/
- https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm
- https://realpython.com/how-to-implement-python-stack/
