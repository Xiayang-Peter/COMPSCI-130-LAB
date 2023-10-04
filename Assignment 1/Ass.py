#Student Name: Xia Yang
#UPI: yxia728


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

            
        
class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        #?# Number of piles
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        #?# returns out the specific line of number based on pile index i             
        return self.piles[i]
    
    def display(self):
        for i in range(self.num_piles):
            print(f"{i}: {self.get_pile(i).return_all(i)}")

    def move(self, p1 = 0, p2 = 0):
        if p1 == p2 == 0:
            #?# p1 = p2 = 0, move the first digit all the way to the back
            for i in range(self.get_pile(p1).size() - 1):
                #?# When move to last index, loop stop 
                self.get_pile(p1).items[i], self.get_pile(p1).items[i + 1] = self.get_pile(p1).items[i + 1], self.get_pile(p1).items[i]
        elif (p1 == 0 < p2) and not self.get_pile(p1).is_empty():
            #?# Make sure p1 is not empty
            try:
                #?# Condition1: (last number of p2) - 1 == (first number of p1)
                #?# Condition2: p1 is not empty
                if self.get_pile(p2).peek_bottom() - 1 == self.get_pile(p1).peek_top():
                    #?# Condition1 met and condition2 met
                    self.get_pile(p2).add_bottom(self.get_pile(p1).remove_top())
            except IndexError:
                #?# Condition1 doesn't exist when p2 is empty and condition2 met
                self.get_pile(p2).add_bottom(self.get_pile(p1).remove_top())
        elif (p1 and p2) > 0 and not self.get_pile(p1).is_empty() and not self.get_pile(p2).is_empty():
            #?# Make sure both p1 and p2 are not empty
            if self.get_pile(p2).peek_bottom() - 1 == self.get_pile(p1).peek_top():
                for p1_elements in (self.get_pile(p1).remove_all()):
                    self.get_pile(p2).add_bottom(p1_elements)
        else: #?# if move not vaild, ignore
            pass

    def is_complete(self):
        for i in range(self.num_piles):
            listed_pile_i = self.get_pile(i).return_item_list()
            if len(listed_pile_i) == self.num_cards and i != 0 :
                for index in range(len(listed_pile_i)):
                    if listed_pile_i[index] == listed_pile_i[-1]:
                        return True
                    elif (listed_pile_i[index] - 1) == listed_pile_i[index + 1]:
                        pass
                    else:
                        return False
        else:
            return False

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            move_number += 1
            
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")


