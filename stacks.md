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

## Coding Examples

### **Code Example of a Stack in Python**

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

### **Program Example of a Stack in Python**

```python
'''
    This simple program will keep track of your
    Tasks/Todos in a LIFO (Last In First Out) order.

    Although, todo list tend to work in a really any order,
    I found this program nice to help understand how a Stack
    could be implemented.

    Program written by Matthew Rapp.
'''


class Tasks:
    def __init__(self):
        self.tasks = []

    # add_task method allows you to add a
    # task to the front of the list
    def add_task(self, task):
        # if the task is already in the stack, return False
        if task in self.tasks:
            return False

        # if the task is not in the stack, add the task
        self.tasks.append(task)
        return True

    # remove_current_task method allows you to remove
    # the current task when finished or not needed
    def remove_current_task(self):
        # if there is no tasks in the task stack, just return
        if len(self.tasks) <= 0:
            return

        # if there is a task in the stack, pop off the current task
        return self.tasks.pop()

    # next_task method allows you to see what is
    # next to do, in order of priority
    def next_task(self):
        print(self.tasks[-1])
        return


todos = Tasks()
todos.add_task('yo yo')
todos.add_task('need clothes')
todos.next_task()  # Output: need clothes
todos.add_task('drive to grocery store')
todos.next_task()  # Output: drive to grocery store
todos.remove_current_task()
todos.add_task('get ice cream')
todos.remove_current_task()
todos.remove_current_task()
todos.next_task()  # Output: yo yo
```

## Problem To Solve

For this problem, we will expand on the example program written above. The requirements for this problem include:

1. A _reverse_ method within the class to reverse the tasks, just if someone wanted to view the tasks in order they were written in.
1. A _see_all_tasks_ method within the class if the user wants to see all the tasks left to do.
1. An _is_empty_ method that will return True or False depending on if there are more tasks within the todo list.
1. An _undo_ method that allows the user to undo the last action that was executed. HINT: you will want the user to be able to undo anything that has been done within the program, meaning more than just one undo.

Be sure to leave relavent, concise comments throughout the code you write. It's good practice and will benefit you in the future when referencing back on old code or if someone wanted to look over your code.

Code to start out with (feel free to copy and paste into your own file):

```python
class TodoList:
    def __init__(self):
        self.tasks = []
        self.history = []

    # add_task method allows you to add a task to the front of the list
    def add_task(self, task):
        # if the task is already in the stack, return False
        if task in self.tasks:
            return False

        # add that task to the history
        self.history.append(('add', task))
        # if the task is not in the stack, add the task
        self.tasks.append(('add', task))
        return True

    # remove_current_task method allows you to remove the current task when finished or not needed
    def remove_current_task(self):
        # if there is no tasks in the task stack, just return
        if len(self.tasks) <= 0:
            return
        # if there is a task in the stack, pop off the current task
        taskToDelete = self.tasks.pop()
        # add that task to the history
        self.history.append(('remove', taskToDelete[1]))
        return

    # next_task method allows you to see what is next to do, in order of priority
    def next_task(self):
        print(self.tasks[-1][1])
        return

    #####################
    # Problem #1
    #####################
    def reverse(self):
        ''' Your code goes here '''
        pass

    #####################
    # Problem #2
    #####################
    def see_all_tasks(self):
        ''' Your code goes here '''
        pass

    #####################
    # Problem #3
    #####################
    def is_empty(self):
        ''' Your code goes here '''
        pass

    #####################
    # Problem #4
    #####################
    def undo(self):
        ''' Your code goes here '''
        pass


todos = TodoList()
todos.add_task('yo yo')
todos.add_task('need clothes')
todos.add_task('drive to grocery store')
todos.next_task()  # Output: drive to grocery store
print('===============')
todos.remove_current_task()

##################
### Problem #1 ###
##################
todos.reverse()  # Output: ['yo yo', 'need clothes']
print('===============')
##################
##################
##################
todos.add_task('need buttermilk')
todos.add_task('catch a pokemon')
todos.add_task('watch movie')
##################
### Problem #2 ###
##################
# Output: ['watch movie', 'catch a pokemon', 'need buttermilk', 'need clothes', 'yo yo']
todos.see_all_tasks()
print('===============')
##################
##################
##################
todos.remove_current_task()
todos.remove_current_task()
##################
### Problem #3 ###
##################
todos.is_empty()  # Output: False
print('===============')
##################
##################
##################
todos.next_task()  # Output: need buttermilk
todos.add_task('superbowl party')
print('===============')
##################
### Problem #4 ###
##################
todos.next_task()  # Output: superbowl party
# Output: ['superbowl party', 'need buttermilk', 'need clothes', 'yo yo']
todos.see_all_tasks()
todos.undo()
todos.next_task()  # Output: need buttermilk
print('===============')
todos.undo()
# Output: ['catch a pokemon', 'need buttermilk', 'need clothes', 'yo yo']
todos.see_all_tasks()
print('===============')
```

You can check your answer with the solution here: [Solution](stack-problem.py)

## Resources

- https://www.geeksforgeeks.org/stack-data-structure/
- https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm
- https://realpython.com/how-to-implement-python-stack/
