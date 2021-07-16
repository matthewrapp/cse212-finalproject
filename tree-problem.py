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
        if data < root.data:
            if root.left is None:
                print('False')
                return False
            else:
                return self._exists(data, root.left)
        elif data > root.data:
            if root.right is None:
                print('False')
                return False
            else:
                return self._exists(data, root.right)
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
        # implement your code here
        current = root
        if current.left is not None:
            current = self._get_min(current.left)
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
        # implement your code here
        current = root
        if current.right is not None:
            current = self._get_max(current.right)
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
        # implement your code here
        # print('first print: ', data, root.data)
        if data < root.data:
            # print('data < root.data: ', data, root.data,
            #       root.left.data, root.right.data)
            if root.left is None:
                return False
            else:
                return self._delete(data, root.left)
        elif data > root.data:
            # print('data > root.data: ', data, root.data,
            #       root.left.data, root.right.data)
            if root.right is None:
                return False
            else:
                return self._delete(data, root.right)
        else:
            # print('data == root.data: ', data,
            #       root.data, root.left, root.right)
            # this is the node to be deleted
            if root.left is None:
                # print('root.left == None: ', data,
                #       root.data, root.left, root.right)

                temp = root.right
                root = None
                return temp

            elif root.right is None:
                # print('root.right == None: ', data,
                #       root.data, root.left, root.right)
                temp = root.left
                root = None
                return temp

            # print('root.left != None && root.right != None: ', data, root)
            # if there is still a left and right child to the node being deleted, take the minimum value in the right subtree and make that the root
            temp = self._get_min(root.right)
            root.data = temp.data
            # delete the node successor
            print('here: ', temp.data, root.right)
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
        # implement your code here
        if root is None:
            return False
        else:
            if self._height(root.left) > self._height(root.right):
                return self._height(root.left) + 1
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
        # implement your code here
        pass

    ##################
    ##################
    ##################


# create an tree instance
numbers = [3, 25, 1]
tree = BST()
for num in numbers:
    tree.insert(num)
# for node in tree:
#     print(node)  # Output: 1, 3, 25
# tree.exists(22)  # Output: False
# tree.exists(25)  # Output: True

### Problem #1 ###
tree.delete(1)
print('')
for node in tree:
    print(node)  # Output: 3, 25
print('_______________\n')
minNode = tree.get_min()
print('Min Value: ', minNode.data)
print('_______________\n')
maxNode = tree.get_max()
print('Max Value: ', maxNode.data)
print('_______________\n')
th = tree.height()
print('Tree Height: ', th)  # Output 2
print('_______________\n')
