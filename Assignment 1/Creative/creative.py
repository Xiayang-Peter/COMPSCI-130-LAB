
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

    def window_test(self, App_return):
        if App_return == 1:
            return("1")
        if App_return == 2:
            return("2")
    
    def play_new(self):
        returned_display = ""
        for i in range(self.num_piles):
            returned_display += (f"{i}: {self.get_pile(i).return_all(i)}\n")
        return returned_display






import sv_ttk
import tkinter
from tkinter import ttk
import tkinter as tk1
#import tkinter.font as tkFont

class App:
    def __init__(self, root, cards):
        # init the game from Solitaire
        global solitaire_game
        solitaire_game = Solitaire(cards)
        
        #setting title
        root.title("undefined")
        #setting window size
        width=944
        height=538
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        root.geometry(f"{screenwidth // 2}x{screenheight // 2}")
        root.resizable(width=False, height=False)

        button_trigger1=ttk.Button(root)
        #button_trigger1["anchor"] = "center"
        #button_trigger1["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #button_trigger1["font"] = ft
        #button_trigger1["fg"] = "#000000"
        #button_trigger1["justify"] = "center"
        #button_trigger1["relief"] = "flat"
        button_trigger1["text"] = "return 1"
        button_trigger1.place(x=screenwidth//4,y=370,width=70,height=25)
        button_trigger1["command"] = self.button_trigger1_command
        
        button_trigger2=ttk.Button(root)
        #button_trigger2["anchor"] = "center"
        #button_trigger2["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #button_trigger2["font"] = ft
        #button_trigger2["fg"] = "#000000"
        #button_trigger2["justify"] = "center"
        button_trigger2["text"] = "return 2"
        #button_trigger2["relief"] = "flat"
        button_trigger2.place(x=screenwidth//4,y=280,width=70,height=25)
        button_trigger2["command"] = self.button_trigger2_command

        button_trigger3=ttk.Button(root)
        #button_trigger3["anchor"] = "center"
        #button_trigger3["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #button_trigger3["font"] = ft
        #button_trigger3["fg"] = "#000000"
        #button_trigger3["justify"] = "center"
        button_trigger3["text"] = ""
        button_trigger3.place(x=screenwidth//4,y=310,width=70,height=56)
        button_trigger3["command"] = self.button_trigger3_command

        button_color_trigger1 = ttk.Button(root)
        button_color_trigger1["text"] = "Change Theme!"
        button_color_trigger1["command"] = sv_ttk.toggle_theme
        button_color_trigger1.place(x=screenwidth//4 - 15,y=400,width=100,height=25)

        message_box1=tk1.Message(root)
        #message_box1["anchor"] = "center"
        #ft = tkFont.Font(family='Times',size=10)
        #message_box1["font"] = ft
        #message_box1["fg"] = "#000000"
        #message_box1["bg"] = "#f0f0f0"
        #message_box1["justify"] = "center"
        message_box1["text"] = solitaire_game.play_new()
        #message_box1["relief"] = "sunken"
        message_box1.place(x=(screenwidth//4) - 100,y=30,width=296,height=231)


    def color_inverse(self):
        theme_color = sv_ttk.get_theme()
        if theme_color == "light":
            print("light")
            return "dark"
        elif theme_color == "dark":
            print("dark")
            return "light"

    def button_trigger1_command(self):
        print("command")

    def button_trigger2_command(self):
        print("command")


    def button_trigger3_command(self):
        print("command")


root = tkinter.Tk()
app = App(root,[1,2,3,4,5,6,7,8])
sv_ttk.use_dark_theme() 
root.mainloop()
