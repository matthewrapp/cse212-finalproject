# Python code to help demonstrate the usage of a Tree and help improve your knowledge and skills of a Tree.

class BST:
    # implement the Binary Search Tree data structure.  The Node class below is an inner class to create a node/data object

    class Node:
        # each node of the BST will have data/data object and pointers to the left and right sub-tree

        def __init__(self, data=None):
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        # initialize an empty BST
        self.root = None

    def insert(self, data):
        if self.root is None:
            # this means that the tree is empty, so just create a node within the tree
            self.root = BST.Node(data)
        else:
            # call a private function to implement the node into the right place within the tree. We use this function recursively.
            self._insert(data, self.root)

    def _insert(self, data, root):
        # this method will look for a place to insert a node/data object

        # if data is smaller than root
        if data < root.data:
            # if left side of tree is empty, insert a new node there
            if root.left is None:
                root.left = BST.Node(data)
            # if it's not empty, recurse to keep going down the tree
            else:
                self._insert(data, root.left)
        # if data is larger than root
        else:
           # if right side of tree is empty, insert a new node there
            if root.right is None:
                root.right = BST.Node(data)
            # if it's not empty, recurse to keep going down the tree
            else:
                self._insert(data, root.right)

    def exists(self, data):
        # this method will search for a node that contains data within the BST
        # by calling the private class mathod to recurse through the tree
        return self._exists(data, self.root)  # Start at the root

    def _exists(self, data, root):
        # this method will search for a node that contains data within the BST
        # if not found, it will return False or recurse again
        # if found, it will return True

        # if data is less than the root.data (left side)
        if data < root.data:
            # if the root has no Node on left side, return False
            if root.left is None:
                print('False')
                return False
            # otherwise, recurse with the left root
            else:
                return self._exists(data, root.left)
        # if data is greater than the root.data (right side)
        elif data > root.data:
            # if the root has no Node on right side, return False
            if root.right is None:
                print('False')
                return False
            # otherwise, recurse with the right root
            else:
                return self._exists(data, root.right)
        # if data is equal to the root.data
        else:
            print('True')
            return True

    def get_min(self):
        # this method will return the smallest node in the ree
        if self.root is None:
            return False
        return self._get_min(self.root)  # Start from the root

    ##################
    ### Problem #1 ###
    ##################

    def _get_min(self, root):
        # set current the the root/node being passed in
        current = root
        # if the current.left child exists, recurse with the left child as the root/node
        if current.left is not None:
            current = self._get_min(current.left)
        # return the min value
        return current

    ##################
    ##################
    ##################

    def get_max(self):
        # this method will return the smallest node in the ree
        if self.root is None:
            return False
        return self._get_max(self.root)  # Start from the root

    ##################
    ### Problem #2 ###
    ##################

    def _get_max(self, root):
        # set current the the root/node being passed in
        current = root
        # if the current.right child exists, recurse with the right child as the root/node
        if current.right is not None:
            current = self._get_max(current.right)
        # return the max value
        return current

    ##################
    ##################
    ##################

    def delete(self, data):
        # this method will delete the specificied data out of the tree
        if self.root is None:
            return False
        return self._delete(data, self.root)  # Start at the root

    ##################
    ### Problem #3 ###
    ##################

    def _delete(self, data, root):
        if root is None:
            return root
        # if data being passed in is less than it's root (left side)
        if data < root.data:
            # set the left side of the root to the recursed return
            root.left = self._delete(data, root.left)
        # if data being passed in is greater than it's root (right side)
        elif data > root.data:
            # set the right side of the root to the recursed return
            root.right = self._delete(data, root.right)
        # if data being passed in is equal than it's root
        # this is the node to be deleted
        else:
            if root.left is None:
                # set temperary variable to the right side
                temp = root.right
                # set the root to None
                root = None
                # return the temperary variable
                return temp

            elif root.right is None:
                # set temperary variable to the left side
                temp = root.left
                # set the root to None
                root = None
                # return the temperary variable
                return temp

            # if there is still a left and right child to the node being deleted,
            # take the minimum value in the right subtree and make that the root
            temp = self._get_min(root.right)
            root.data = temp.data
            # delete the node successor
            root.right = self._delete(temp.data, root.right)

        return root

    ##################
    ##################
    ##################

    def height(self):
        # this method is called when wanting to know the tree's height
        if self.root is None:
            return False
        else:
            return self._height(self.root)  # Start at the root

    ##################
    ### Problem #4 ###
    ##################

    def _height(self, root):
        # if the root is None, nothing in tree, return
        if root is None:
            return False
        # otherwise, there is at least 1 node in the tree
        else:
            # if the height of the left side of the root is greater than the height of the right side of the root, return the left side + 1
            if self._height(root.left) > self._height(root.right):
                return self._height(root.left) + 1
            # otherwise, return the right side + 1
            else:
                return self._height(root.right) + 1

    ##################
    ##################
    ##################

    def __iter__(self):
        # forward traversal
        # this method is called when a loop is performed
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, root):
        # print out data, from smallest to largest
        # if the root is not equal to None
        if root is not None:
            yield from self._traverse_forward(root.left)
            yield root.data
            yield from self._traverse_forward(root.right)

    def __reversed__(self):
        # backward traversal
        # this method is called when a loop is called on reversed() method
        yield from self._traverse_backward(self.root)  # Start at the root

    ##################
    ### Problem #5 ###
    ##################

    def _traverse_backward(self, root):
        # print out data, from largest to smallest
        # if the root is not equal to None
        if root is not None:
            yield from self._traverse_backward(root.right)
            yield root.data
            yield from self._traverse_backward(root.left)

    ##################
    ##################
    ##################


# create an tree instance
numbers = [3, 25, 1, 20]
tree = BST()
print('\nNumbers in Tree:')
for num in numbers:
    tree.insert(num)
for node in tree:
    print(node)  # Output: 1, 3, 20, 25
print('_______________\n')
tree.exists(22)  # Output: False
print('_______________\n')
tree.exists(25)  # Output: True
print('_______________\n')

### Problem #1 ###
minNode = tree.get_min()
print('Problem #1, Min Value: ', minNode.data)
print('_______________\n')
##################

### Problem #2 ###
maxNode = tree.get_max()
print('Problem #2, Max Value: ', maxNode.data)
print('_______________\n')
##################

### Problem #3 ###
print('Problem #3, Values in Tree after deletion: ')
tree.delete(20)
for node in tree:
    print(node)  # Output: 1, 3, 25
print('_______________\n')
##################

### Problem #4 ###
th = tree.height()
print('Problem #4, Tree Height: ', th)  # Output 2
print('_______________\n')
##################

### Problem #5 ###
print('Problem #5, Tree values from largest to smallest: ')  # Output 2
for node in reversed(tree):
    print(node)  # Output: 25, 20, 1
print('_______________\n')
##################
