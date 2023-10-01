from Class import *
import sv_ttk
from tkinter import ttk
import tkinter as tk1
import random

class App:
    def __init__(self, root):


    #?# This is the string for GUI game rule
        self.rules = """(`0`)\n
 ____________________________________
|                                    |
|    Hello ! I am Rule !!!!          |
|And I will tell you how to play this|
|____________________________________|
 * This game is made my Peter for his COMPSCI 130 Assignment
 * The rules is simple:\n\nYou can only move the first digit of one pile to the last digit of another pile when first digit is exactly 1 less than current last digit of another pile.
But also you can swap the first and the last digit for the first pile !\n\n don't try to delete me, something bad would happen !"""
    #?# This is the string for GUI game rule

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
#        self.screenwidth = self.root.winfo_screenwidth()
#        self.screenheight = self.root.winfo_screenheight()
        self.screenwidth = 1920
        self.screenheight = 1080
        self.root.geometry(f"{self.screenwidth // 2}x{self.screenheight // 2}")
        self.root.resizable(width=False, height=False)
        #setting window size
        self.one_quarter_screenwidth = self.screenwidth // 4
        self.one_quarter_screenheight = self.screenheight // 4
        self.button_start_position_x = self.screenwidth // 10
        self.button_start_position_y = 280

        #?# Main game window 
        self.message_box1=tk1.Message(self.root)
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        self.message_box1["relief"] = "sunken"
        self.message_box1.place(x=self.button_start_position_x - 100,y=30,width=296,height=231)
        #?# Main game window 
        
        #?# information box trigger
        self.button_trigger4 = ttk.Button(self.root)
        self.button_trigger4["command"] = self.disable_information_box
        self.button_trigger4["text"] = "Hide debug window and rules"
        self.button_trigger4.place(x=self.button_start_position_x - 70,y=self.button_start_position_y,width=226,height=30)
        #?# information box trigger

        self.button_trigger2=ttk.Button(self.root)
        self.button_trigger2["text"] = "Restart game"
        self.button_trigger2.place(x=self.button_start_position_x - 5,y=self.button_start_position_y + 35,width=75,height=30)
        self.button_trigger2["command"] = self.button_trigger2_command

        #?#  Entry Box set with lable
        self.entry_1 = ttk.Entry(self.root)
        self.entry_1.place(x=self.button_start_position_x - 15,y=self.button_start_position_y + 70,width=100,height=30)

        self.entry_1_lable_1 = ttk.Label(self.root)
        self.entry_1_lable_1["text"] = "from: "
        self.entry_1_lable_1.place(x=self.button_start_position_x - 60,y=self.button_start_position_y + 70,width=40,height=30)

        self.entry_2 = ttk.Entry(self.root)
        self.entry_2.place(x=self.button_start_position_x - 15,y=self.button_start_position_y + 105,width=100,height=30)

        self.entry_2_lable_1 = ttk.Label(self.root)
        self.entry_2_lable_1["text"] = "to: "
        self.entry_2_lable_1.place(x=self.button_start_position_x - 55,y=self.button_start_position_y + 105,width=40,height=30)
        #?#  Entry Box set with lable

        self.button_trigger3 = ttk.Button(self.root)
        self.button_trigger3["text"] = "Run Step"
        self.button_trigger3.place(x=self.button_start_position_x - 5,y=self.button_start_position_y + 140,width=80,height=30)
        self.button_trigger3["command"] = self.button_trigger3_command

        self.button_color_trigger1 = ttk.Button(self.root)
        self.button_color_trigger1["text"] = "Change Theme!"
        self.button_color_trigger1["command"] = self.color_inverse
        self.button_color_trigger1.place(x=self.button_start_position_x - 20,y=self.button_start_position_y + 175,width=100,height=30)

        self.button_trigger3_restrict_mode = ttk.Button(self.root)
        self.button_trigger3_restrict_mode.place(x=self.button_start_position_x - 40,y=self.button_start_position_y + 210,width=150,height=30)
        self.button_trigger3_restrict_mode["text"] = "enter restrict mode"
        self.button_trigger3_restrict_mode["command"] = self.button_trigger3_restrict_mode_command


        #!# information_box
        self.message_box2_rules=tk1.Text(self.root)
        self.message_box2_rules["relief"] = "sunken"
        self.message_box2_rules.insert(1.0,self.rules)
        self.message_box2_rules.place(x=self.screenwidth // 2 - 400, y=0, width = 400, height = self.one_quarter_screenheight)


        self.message_box3_debug_window=tk1.Text(self.root)
        self.message_box3_debug_window["relief"] = "sunken"
        self.message_box3_debug_window.place(x=self.screenwidth // 2 - 400, y=self.one_quarter_screenheight, width = 400, height = self.one_quarter_screenheight)
        #!# information_box
        
    def surprise(self):
        if self.message_box2_rules.get(1.0,"end") != f"{self.rules}\n":
            self.message_box2_rules.delete('1.0', "end")
            self.message_box2_rules.insert("end","      ________________________        /(ಠ_ಠ/)\n     |                        |\n     |WHY RU DELETING ME????? |       **PLONK**\n     |________________________|")
    
    def disable_information_box(self):
        self.surprise()
        if self.hide_status:
            self.message_box2_rules.place(x=self.screenwidth // 2 - 400, y=0, width = 400, height = self.one_quarter_screenheight)
            self.message_box3_debug_window.place(x=self.screenwidth // 2 - 400, y=self.one_quarter_screenheight, width = 400, height = self.one_quarter_screenheight)
            self.hide_status = False
            self.button_trigger4["text"] = "Hide debug window and rules"
            self.print_message(f"Enable information box")

        else:
            self.message_box3_debug_window.place_forget()
            self.message_box2_rules.place_forget()
            self.hide_status = True
            self.button_trigger4["text"] = "Unhide debug window and rules"
            self.print_message(f"Disable information box")


    def color_inverse(self):
        self.surprise()
        theme_color: str = sv_ttk.get_theme()
        if theme_color == "light":
            sv_ttk.use_dark_theme()
            self.print_message("Set color to Dark")
            return "dark"
        elif theme_color == "dark":
            sv_ttk.use_light_theme()
            self.print_message("Set color to Light")
            return "light !"

    def button_trigger2_command(self):
        self.surprise()
        self.cards = self.cards = random.sample(range(1,7), 6)
        self.solitaire_game = Solitaire(self.cards)
        self.restrict_mode = False
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        self.button_trigger3_restrict_mode["text"] = "enter restrict mode"
        self.print_message("Game restarted")


    def button_trigger3_command_restrict_mode(self):
        self.surprise()
        #?# New function for restrict mode to be harder without any error message 
        move_from = self.entry_1.get()
        move_to = self.entry_2.get()
        self.solitaire_game.GUI_move(move_from,move_to)
        self.message_box1["text"] = self.solitaire_game.GUI_display()
        self.print_message(f"move from pile: {move_from} to pile: {move_to}")

    def button_trigger3_command(self):
        self.surprise()
        try:
            move_from = int(self.entry_1.get())
            move_to = int(self.entry_2.get())
            states = self.solitaire_game.GUI_move(move_from,move_to)
            if states:
                self.message_box1["text"] = self.solitaire_game.GUI_display()
                self.print_message(f"move from pile: {move_from} to pile: {move_to}")
            else:
                self.message_box1["text"] = self.solitaire_game.GUI_display()
                self.print_message("Wrong move, please read rules carefully !")
        except ValueError:
            self.print_message("Pile number must be numbers !")
    
    
    def button_trigger3_restrict_mode_command(self):
        self.surprise()
        if not self.restrict_mode:
            self.solitaire_game = Solitaire(self.cards,max_num_moves = 8,num_piles = 4)
            self.message_box1["text"] = self.solitaire_game.GUI_display()
            self.button_trigger3_restrict_mode["text"] = "exit restrict mode"
            self.restrict_mode = True
            self.button_trigger3["command"] = self.button_trigger3_command_restrict_mode
            self.print_message("Enter restrict mode")
        else:
            self.solitaire_game = Solitaire(self.cards)
            self.message_box1["text"] = self.solitaire_game.GUI_display()
            self.button_trigger3_restrict_mode["text"] = "enter restrict mode"
            self.restrict_mode = False
            self.button_trigger3["command"] = self.button_trigger3_command
            self.print_message("Exit restrict mode")

    def print_message(self,text):
        self.surprise()
        self.message_box3_debug_window.insert("end",text + "\n")
        self.message_box3_debug_window.update()

window = tk1.Tk()
app = App(window)
sv_ttk.use_dark_theme()
window.mainloop()





