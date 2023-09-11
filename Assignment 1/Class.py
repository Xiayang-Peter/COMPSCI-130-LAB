class CardPile:
    def __init__(self):
        self.items = []
    def add_top(self, item):
        self.items.insert(0,item)
    def add_bottom(self, item):
        self.items.append(item)
    def remove_top(self):
        removed = self.items[0]
        self.items.pop(0)
        return removed
    def remove_bottom(self):
        removed = self.items[-1]
        self.items.pop(-1)
        return removed
    def size(self):
        return(len(self.items))
    def peek_top(self):
        return(self.items[0])
    def peek_bottom(self):
        return(self.items[-1])
    def print_all(self, index):
        if index == 1:
            output = ""
            for numbers in self.items:
                output += f"{numbers} "
            print(output)
        elif index == 0:
            output = ""
            output += f"{self.items[0]} "
            for i in range(len(self.items) - 1):
                output += "* "
            print(output)
               

        
class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]
    
"""    def display(self):
 
    def move(self, p1, p2):

    def is_complete(self):

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
"""
