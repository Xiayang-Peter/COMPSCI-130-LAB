from Class import *
from creative import * 
import sv_ttk
from tkinter import ttk
import tkinter as tk1
from Class import *


class App:
    def __init__(self, root, cards):
        # init the game from Solitaire
        self.cards = cards
        global solitaire_game
        solitaire_game = Solitaire(self.cards)
        
        #setting title
        root.title("Simple Solitaire Game :)")
        #setting window size

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        root.geometry(f"{screenwidth // 2}x{screenheight // 2}")
        root.resizable(width=False, height=False)


########button_trigger1=ttk.Button(root)
#########button_trigger2["anchor"] = "center"
#########button_trigger2["bg"] = "#f0f0f0"
#########ft = tkFont.Font(family='Times',size=10)
#########button_trigger2["font"] = ft
#########button_trigger2["fg"] = "#000000"
#########button_trigger2["justify"] = "center"
########button_trigger1["text"] = "B1"
#########button_trigger2["relief"] = "flat"
########button_trigger1.place(x=screenwidth//4,y=280,width=70,height=25)
########button_trigger1["command"] = self.button_trigger1_command

        button_trigger2=ttk.Button(root)
        #button_trigger3["anchor"] = "center"
        #button_trigger3["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #button_trigger3["font"] = ft
        #button_trigger3["fg"] = "#000000"
        #button_trigger3["justify"] = "center"
        button_trigger2["text"] = "Refresh"
        button_trigger2.place(x=screenwidth//4,y=310,width=70,height=56)
        button_trigger2["command"] = self.button_trigger2_command

#########button_trigger3=ttk.Button(root)
#########button_trigger1["anchor"] = "center"
#########button_trigger1["bg"] = "#f0f0f0"
#########ft = tkFont.Font(family='Times',size=10)
#########button_trigger1["font"] = ft
#########button_trigger1["fg"] = "#000000"
#########button_trigger1["justify"] = "center"
#########button_trigger1["relief"] = "flat"
########button_trigger3["text"] = "B3"
########button_trigger3.place(x=screenwidth//4,y=370,width=70,height=25)
########button_trigger3["command"] = self.button_trigger3_command

        button_color_trigger1 = ttk.Button(root)
        button_color_trigger1["text"] = "Change Theme!"
        button_color_trigger1["command"] = sv_ttk.toggle_theme
        button_color_trigger1.place(x=screenwidth//4 - 15,y=460,width=100,height=25)

        self.entry_1 = ttk.Entry(root)
        self.entry_1.place(x=screenwidth//4 - 15,y=370,width=100,height=25)

        self.entry_2 = ttk.Entry(root)
        self.entry_2.place(x=screenwidth//4 - 15,y=400,width=100,height=25)

        self.entry_1_lable_1 = ttk.Label(root)
        self.entry_1_lable_1["text"] = "from: "
        self.entry_1_lable_1.place(x=screenwidth//4 - 60,y=370,width=40,height=25)

        self.entry_2_lable_1 = ttk.Label(root)
        self.entry_2_lable_1["text"] = "to: "
        self.entry_2_lable_1.place(x=screenwidth//4 - 55,y=400,width=40,height=25)

        button_trigger3 = ttk.Button(root)
        button_trigger3["text"] = "B3"
        button_trigger3.place(x=screenwidth//4,y=430,width=70,height=25)
        button_trigger3["command"] = self.button_trigger3_command

        button_trigger3_restrict_mode = ttk.Button(root)
        button_trigger3_restrict_mode.place(x=screenwidth//4 - 40,y=490,width=150,height=25)
        button_trigger3_restrict_mode["text"] = "restrict_mode"
        button_trigger3_restrict_mode["command"] = self.button_trigger3_restrict_mode_command

        self.message_box1=tk1.Message(root)
        self.message_box1["text"] = solitaire_game.GUI_display()
        self.message_box1["relief"] = "sunken"
        self.message_box1.place(x=(screenwidth//4) - 100,y=30,width=296,height=231)
        #message_box1["anchor"] = "center"
        #ft = tkFont.Font(family='Times',size=10)
        #message_box1["font"] = ft
        #message_box1["fg"] = "#000000"
        #message_box1["bg"] = "#f0f0f0"
        #message_box1["justify"] = "center"


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
        solitaire_game.GUI_restart_game()
        self.message_box1["text"] = solitaire_game.GUI_display()


    def button_trigger3_command(self):
        move_from = int(self.entry_1.get())
        move_to = int(self.entry_2.get())
        solitaire_game.GUI_move(move_from,move_to)
        self.message_box1["text"] = solitaire_game.GUI_display()
        print(f"move_from:{move_from} to {move_to}")
    
    def button_trigger3_restrict_mode_command(self):
        solitaire_game = Solitaire(self.cards,len(self.cards))
        self.message_box1["text"] = solitaire_game.GUI_display()
    #def get_number_list(self):




