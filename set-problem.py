'''
    This is a program to create a grocery list.

    Although, a grocery list could prioritize order more than a Set does, I felt
    it is a good, easy application to implement as a Set. Once you solve this program,
    you'll find your understanding of a Set Data Strucutre clearer.

    Program written by Matthew Rapp.
'''


class My_Groceries():
    def __init__(self, setOfItems=None):
        # defaults to None
        if setOfItems is None:
            self.grocery_list = set()
        # pass in a set, the grocery list is now equal to the set
        else:
            self.grocery_list = setOfItems

    # this method allows the user to add an item to the set
    def add_item(self, item, price):
        # convert the item and price into a tuple
        storeItem = (item, price)
        # add the tuple to the set
        self.grocery_list.add(storeItem)

    # this method allows the user to remove an item from the set
    def remove_item(self, itemName):
        # copy the set to avoid RuntimeError
        gl = self.grocery_list.copy()
        for item in gl:
            # if item[0], the key/name, is equal to the paramater passed in, then remove it from the grocery list
            if item[0] == itemName:
                self.grocery_list.remove(item)

    ####################
    #### Problem #1 ####
    ####################
    # this method allows the user to see one item at a time within the set
    def get_next_item(self):
        # print out the first item, no order, of the set, then return
        for item in self.grocery_list:
            print(item)
            return
    ####################
    ####################
    ####################

    ####################
    #### Problem #2 ####
    ####################
    # this method allows the user to see the price of the item being passed in
    def get_price(self, itemName):
        for item in self.grocery_list:
            # if the item name/key is equal to the itemName being passed it, bring out the price/value, then return
            if item[0] == itemName:
                print(item[1])
                return
    ####################
    ####################
    ####################

    def _get_item_details(self, itemName):
        for item in self.grocery_list:
            # if the item name/key is equal to the itemName being passed it, bring out the item detials, then return
            if item[0] == itemName:
                print(item)
                return

    ####################
    #### Problem #3 ####
    ####################
    # this method allows the user to update an item within a set
    def update_item(self, oldItemName, updatedItemName, updatedPrice):
        # copy the set to avoid RuntimeError
        gl = self.grocery_list.copy()
        for item in gl:
            if item[0] == oldItemName:
                self.remove_item(oldItemName)
                self.add_item(updatedItemName, updatedPrice)
                self._get_item_details(updatedItemName)
                return
    ####################
    ####################
    ####################

    ####################
    #### Problem #4 ####
    ####################
    # this method allows the user to see the items that are the same within two sets
    def get_intersected_items(self, otherSet):
        # create another set based on self.set and the otherSet passed in
        set3 = self.grocery_list & otherSet
        # print the set
        print(set3)
    ####################
    ####################
    ####################

    ####################
    #### Problem #5 ####
    ####################
    # this method allows the user to combine two sets, without duplicates and returns it as a single set
    def combine_items(self, otherSet):
        # create another set based on self.set and the otherSet passed in
        set3 = self.grocery_list | otherSet
        # return the combined set
        return set3
    ####################
    ####################
    ####################

    # this method returns the grocery list, without printing the items

    def get_grocery_list(self):
        return self.grocery_list

    # this method prints the grocery list
    def see_grocery_list(self):
        print(self.grocery_list)


groceries = My_Groceries()
groceries.add_item('Bananas', 0.89)
groceries.add_item('Milk', 1.12)
groceries.add_item('Sugar', 2.44)
print('================')
# Output: {('Milk', 1.12), ('Bananas', 0.89), ('Sugar', 2.44)}
groceries.see_grocery_list()
print('================')
groceries.remove_item('Sugar')
groceries.see_grocery_list()  # Output: {('Milk', 1.12), ('Bananas', 0.89)}
print('================')
groceries.add_item('Cereal', 3.11)

####################
#### Problem #1 ####
####################
# Output: ('Cereal', 3.11) <-- Due to unorder of things, it could be any tuple printing out
groceries.get_next_item()
print('================')
####################
####################
####################
groceries.add_item('Cookies', 4.56)

####################
#### Problem #2 ####
####################
groceries.get_price('Cereal')  # Output: 3.11
print('================')
####################
####################
####################

####################
#### Problem #3 ####
####################
# Output: ('Fruit Loops', 4.21)
groceries.update_item('Cereal', 'Fruit Loops', 4.21)
print('================')
####################
####################
####################

newGroceries = My_Groceries()
newGroceries.add_item('Apples', 2.89)
newGroceries.add_item('Milk', 1.12)
newGroceries.add_item('Doritos', 4.99)

####################
#### Problem #4 ####
####################
# Convert class into set
ng = newGroceries.get_grocery_list()
groceries.get_intersected_items(ng)  # Output: {('Milk', 1.12)}
print('================')
####################
####################
####################

####################
#### Problem #5 ####
####################
allGroceries = groceries.combine_items(ng)
newestGroceryList = My_Groceries(allGroceries)
# Output: {('Cookies', 4.56), ('Fruit Loops', 4.21), ('Doritos', 4.99), ('Bananas', 0.89), ('Milk', 1.12), ('Apples', 2.89)}
newestGroceryList.see_grocery_list()
####################
####################
####################
