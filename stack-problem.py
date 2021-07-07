'''
    This simple program will keep track of your
    Tasks/Todos in a LIFO (Last In First Out) order.

    Although, todo list tend to work in a really any order,
    I found this program nice to help understand how a Stack
    could be implemented.

    Program written by Matthew Rapp.
'''


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
    # reverse method allows you to reverse the task list to view all the tasks from oldest to newest
    def reverse(self):
        # create an empty list to help style the output
        valuesToPrint = []
        for tuple in self.tasks:
            # append each value of the tuple to the list
            valuesToPrint.append(tuple[1])
        # print the values
        print(valuesToPrint)

    #####################
    # Problem #2
    #####################
    # see_all_tasks method allows you to look at what is todo within the whole stack
    def see_all_tasks(self):
        # create an empty list to help style the output
        valuesToPrint = []
        for tuple in self.tasks[::-1]:
            # append each value of the tuple to the list
            valuesToPrint.append(tuple[1])
        # print the values
        print(valuesToPrint)

    #####################
    # Problem #3
    #####################
    # is_empty method allows you to see if the stack is empty or not
    def is_empty(self):
        if len(self.tasks) != 0:
            print(False)
            return False
        print(True)
        return True

    #####################
    # Problem #4
    #####################
    # undo method allows you to undo your latest action
    def undo(self):
        # take from the back of the list and get the key of the tuple
        lastTupleAction = self.history[-1][0]
        # if the key === 'add'
        if lastTupleAction == 'add':
            # delete that node from the task list
            self.tasks.pop()
            # delete that node from the history list
            self.history.pop()
        # if the key === 'remove'
        elif lastTupleAction == 'remove':
            # delete that node from the history list
            itemToUndo = self.history.pop()
            # add that node back to the task list
            self.tasks.append(itemToUndo)


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
