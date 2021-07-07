# Sets

## Introduction

### **What is a Set?**

- A Set in a type of Data Structure that stores values.
- A Set doesn't prioritize order.
- A Set won't allow duplicates.
- #### **Hashing**
  - A technique used within this Data Structure, in O(1) time, you're able to:
    - add
    - remove
    - test
- #### **Sparse List**
  - A Sparse List isn't guaranteed to be filled from left to right.
    - Very dependent on how the program is hashing the data and matching it with that particular index.
  - Very different than what is normally used, called a Dynamic Array.
- #### **Error/Conflict Handling**
  - Within a set, depending on how the set is hashing and storing the data, there could be an issue.
  - For Example:
    - Below is an image representing a Set.
    - We have indexes 1-6
    - Depending how the table is being hashed, depends on where the node is stored. Take a look at index 5. Let's say the table is being hashed where each node is a number and depending on what the first number starts with, is where the node with be stored.
      - Node = 11
      - That node will be stored under index 1
      - Node = 39
      - That node will be stored under index 3
  - Well how do we handle a situation once that index is already storing a value? Like if index 2 was already storing a node equal to 25 and then another node equaling 23 goes to be hashed, how can we handle that within a set?
  - There are 2 ways to handle this:
    - #### **Open Addressing**
      - Keep looking until an empty slot is found. Once an empty slot is found, insert/return the node depending on what you're trying to do.
      - Danger to open addressing is pretty obvious. The table may fill up too fast, the table might seem very unoriganized, and it will, eventually, start to lag a bit once the program starts to get bigger and bigger.
    - #### **Seperate Chaining**
      - So instead of moving to the next available key within the table, you create a list, and store that list under the appropriate index.
    - Understanding both, you recognize that both can slow down the program. Instead of the set hashing in O(1), it will start hashing in O(n)
      ![Stack Representaion](images/set-rep-1.jpeg)

### **Purpose for a Set in Real World Application**

- Sets....

<br><br>

## Using A Set in Python

A Stack in Python is represented using a list.

### **Operations used within a Python Set**

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

## Coding Examples

### **Code Example of a Stack in Python**

```python
# Python code to help demonstrate the basics of a stack

# Creating a stack
stack = []
```

### **Program Example of a Stack in Python**

```python
'''

    Program written by Matthew Rapp.
'''


class Tasks:
    def __init__(self):
        self.tasks = []
```

## Problem To Solve

For this problem, we will expand on the example program written above. The requirements for this problem include:

1. ...

```python

```

You can check your answer with the solution here: [Solution](stack-problem.py)

## Resources

- https://www.freecodecamp.org/news/what-is-hashing/#:~:text=Hashing%20means%20using%20some%20function,the%20item%20in%20the%20map.
- https://www.geeksforgeeks.org/hashing-set-3-open-addressing/
