class Node:
   def __init__(self, init_data):
       self.data = init_data
       self.next = None

   def get_data(self):
       return self.data

   def get_next(self):
       return self.next

   def set_data(self, new_data):
       self.data = new_data

   def set_next(self, new_next):
       self.next = new_next

class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        #?# adds a new item to the top of the pile (at items[0]).
        self.items.insert(0,item)

    def add_bottom(self, item):
        #?# This method adds a new item to the bottom of the pile (at items[self.size()-1]).
        self.items.append(item)

    def remove_top(self):
        #?# This method removes and returns an item from the top of the pile (at items[0]).
        removed = self.items[0]
        self.items.pop(0)
        return removed
    
    def remove_bottom(self):
        #?# This method removes and returns an item from the bottom of the pile (at items[self.size()-1]).
        removed = self.items[-1]
        self.items.pop(-1)
        return removed
    
    def clear(self):
        self.items = []

    def remove_all(self):
        #!# CAREFUL THIS FUNCTION DELETE THE PILE AND RETURNS A WHOLE LIST 
        removed_items = self.items
        self.clear()
        return removed_items

    def is_empty(self):
        return self.items == []

    def size(self):
        #?# This method returns the size of the pile.
        return(len(self.items))
    
    def peek_top(self):
        #?# This method returns the top card of the pile (at items[0]).
        return(self.items[0])
    
    def peek_bottom(self):
        #?# This method returns the bottom card of the pile (at items[self.size()-1]).
        #!#return(self.items[self.size() - 1])
        return(self.items[-1])

    def print_all(self, index = 1):               
        if index == 0:
        #?#  when index goes to 1, all numbers printed visible   
            printed_pile = ""
            try:
            #!# improved when pile contains no numbers
                printed_pile += f"{self.items[0]} "
                for i in range(self.size() - 1):
                    printed_pile += "* "
                print(printed_pile)
            except IndexError:
                print()        
        else:           
        #?#  when index goes to 1, all numbers printed visible                                   
            printed_pile = ""
            for digits in self.items:
                printed_pile += f"{digits} "
            print(printed_pile)  

    def return_all(self, index = 1):        
        #?# improvement to the def print_all
        if index == 0:
        #?#  when index goes to 1, all numbers printed visible   
            returned_pile = ""
            try:
                returned_pile += f"{self.items[0]} "
                for i in range(self.size() - 1):
                    returned_pile += "* "
                return returned_pile
            except IndexError:
                return ""
        else:           
        #?#  when index goes to 1, all numbers printed visible                                   
            returned_pile = ""
            for digits in self.items:
                returned_pile += f"{digits} "
            return returned_pile

    def return_item_list(self):
        #?# Returns pile as a list 
        return self.items

            
