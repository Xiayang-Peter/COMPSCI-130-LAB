from Class import *
from creative import * 
import sv_ttk
from tkinter import ttk
import tkinter as tk1
from Class import *
import random


class App:
    def __init__(self, root):
        self.hide_status = False
        #restrict_mode
        self.restrict_mode = False
        # init the game from Solitaire
        self.cards = random.sample(range(1,7), 6)
#       global solitaire_game
#       solitaire_game = Solitaire(self.cards)
        self.solitaire_game = Solitaire(self.cards)
        self.root = root
        
        #setting title
        self.root.title("Simple Solitaire Game :)")
        #setting title
        #setting window size
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screenwidth // 2}x{self.screenheight // 2}")
        self.root.resizable(width=False, height=False)
        #setting window size


        self.button_trigger2=ttk.Button(self.root)
        self.button_trigger2["text"] = "Refresh"
        self.button_trigger2.place(x=self.screenwidth//4,y=310,width=70,height=56)
        self.button_trigger2["command"] = self.button_trigger2_command

        self.button_color_trigger1 = ttk.Button(self.root)
        self.button_color_trigger1["text"] = "Change Theme!"
        self.button_color_trigger1["command"] = sv_ttk.toggle_theme
        self.button_color_trigger1.place(x=self.screenwidth//4 - 15,y=460,width=100,height=25)

        self.entry_1 = ttk.Entry(self.root)
        self.entry_1.place(x=self.screenwidth//4 - 15,y=370,width=100,height=25)

        self.entry_2 = ttk.Entry(self.root)
        self.entry_2.place(x=self.screenwidth//4 - 15,y=400,width=100,height=25)

        self.entry_1_lable_1 = ttk.Label(self.root)
        self.entry_1_lable_1["text"] = "from: "
        self.entry_1_lable_1.place(x=self.screenwidth//4 - 60,y=370,width=40,height=25)

        self.entry_2_lable_1 = ttk.Label(self.root)
        self.entry_2_lable_1["text"] = "to: "
        self.entry_2_lable_1.place(x=self.screenwidth//4 - 55,y=400,width=40,height=25)

        self.button_trigger3 = ttk.Button(self.root)
        self.button_trigger3["text"] = "Run Step"
        self.button_trigger3.place(x=self.screenwidth//4 - 10,y=430,width=80,height=25)
        self.button_trigger3["command"] = self.button_trigger3_command

        self.button_trigger3_restrict_mode = ttk.Button(self.root)
        self.button_trigger3_restrict_mode.place(x=self.screenwidth//4 - 40,y=490,width=150,height=25)
        self.button_trigger3_restrict_mode["text"] = "enter restrict mode"
        self.button_trigger3_restrict_mode["command"] = self.button_trigger3_restrict_mode_command

        self.message_box1=tk1.Message(self.root)
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        self.message_box1["relief"] = "sunken"
        self.message_box1.place(x=(self.screenwidth//4) - 100,y=30,width=296,height=231)

        #!# information_box
        self.message_box2_rules=tk1.Message(self.root)
        self.message_box2_rules["relief"] = "sunken"
        #self.message_box2_rules.place(x=0,y=0,width=296,height = self.screenheight // 2)

        self.message_box3_debug_window=tk1.Message(self.root)
        self.message_box3_debug_window["relief"] = "sunken"
        #self.message_box3_debug_window.place(x=self.screenwidth // 2 - 296,y=0,width=296,height = self.screenheight // 2)

            #?# information box trigger
        self.button_trigger4 = ttk.Button(self.root)
        self.button_trigger4["command"] = self.disable_information_box
        self.button_trigger4["text"] = "Unhide debug window and rules"
        self.button_trigger4.place(x=self.screenwidth//4 - 70,y=280,width=226,height=25)
            #?# information box trigger
        #!# information_box

    def disable_information_box(self):
        print("yes")
        if not self.hide_status:
            self.message_box2_rules.place(x=0,y=0,width=296,height = self.screenheight // 2)
            self.message_box3_debug_window.place(x=self.screenwidth // 2 - 296,y=0,width=296,height = self.screenheight // 2)
            self.hide_status = True
            self.button_trigger4["text"] = "Hide debug window and rules"
            print(f"unhide, current status = {self.hide_status}")
        else:
            self.message_box3_debug_window.place_forget()
            self.message_box2_rules.place_forget()
            self.hide_status = False
            self.button_trigger4["text"] = "Unhide debug window and rules"
            print(f"hide, current status = {self.hide_status}")

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
        print("Refresh")
        self.cards = self.cards = random.sample(range(1,7), 6)
        self.solitaire_game = Solitaire(self.cards)
        self.restrict_mode = False
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        self.button_trigger3_restrict_mode["text"] = "enter restrict mode"


    def button_trigger3_command(self):
        move_from = int(self.entry_1.get())
        move_to = int(self.entry_2.get())
        self.solitaire_game.GUI_move(move_from,move_to)
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        print(f"move_from:{move_from} to {move_to}")
    
    def button_trigger3_restrict_mode_command(self):
        if not self.restrict_mode:
            self.solitaire_game = Solitaire(self.cards,max_num_moves = 8,num_piles = 4)
            self.message_box1["text"] = self.solitaire_game.GUI_display()
            self.button_trigger3_restrict_mode["text"] = "exit restrict mode"
            self.restrict_mode = True
        else:
            self.solitaire_game = Solitaire(self.cards)
            self.message_box1["text"] = self.solitaire_game.GUI_display()
            self.button_trigger3_restrict_mode["text"] = "enter restrict mode"
            self.restrict_mode = False




