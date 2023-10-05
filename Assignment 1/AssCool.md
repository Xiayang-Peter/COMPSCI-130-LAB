***Student Name: Xia Yang***
***UPI: yxia728***
AssCool PDF documentation 


AssCool.py is a impletation of code Ass.py, it only requires python build-in modules tkinter and random to run.
In AssCool.py the class "Solitaire" from Ass.py has been modified.

**What has been modified ?**
I limit the number of cards to 6. While you start a game, the random() will mix the number from 1 to 7 to make a randomlized cards:
```python
self.cards = random.sample(range(1, 7), 6)
```

in function ```def _init_(self)```:
add these
```python
self.current_move_number = 0
self.num_piles = num_piles
self.max_num_moves = max_num_moves
```

in function ```def move(self, p1=0, p2=0)```:
add a new returned value that return False if current move is invalid, else return True 

delete function ```def play(self)```
add ```def GUI_display(self)``` and ```def GUI_move(self, pile1, pile2)``` to support App class ```class App:``` 

-----------------------------
**New App class:**
```self.rules```: game rules
```self.hide_status``` ```self.restrict_mode```: Indicate status of rule window and restrict mode, default is False

Buttons and commands:
```self.message_box1``` $\rightarrow$    ```self.solitaire_game.GUI_display()```
Usage: Print piles and status on message box

```self.button_trigger1``` $\rightarrow$ ```self.disable_information_box```
Usage: Hide debug window and rule window
```self.button_trigger2``` $\rightarrow$ ```self.button_trigger2_command```
Usage: Restart game 

```self.button_trigger3``` $\rightarrow$ ```self.button_trigger3_command```
Usage: Get pile number from entry_1 and entry_2 and run Solitaire

```self.button_trigger4``` $\rightarrow$ ```self.button_trigger4_command```
Usage: Enable and disable restrict mode

```self.entry_1_lable_1```  $\rightarrow$ ```self.entry_1``` 
```self.entry_2_lable_1``` $\rightarrow$ ```self.entry_2``` 

**What does restrict mode have ?**
* round reduced from 12 to 8
* piles reduced from 5 to 4
* if you didn't enter a number as pile number or wrong move, there will be no output and round will still increase

**Other stuff:**
* if you uncomment the code and download pip package sv_ttk, the window will looks better with changeable theme
* ```def surprise(self)``` is a function where if you delete rules, print new rules