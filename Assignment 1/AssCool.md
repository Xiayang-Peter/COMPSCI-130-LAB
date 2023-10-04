***Student Name: Xia Yang***
***UPI: yxia728***
AssCool PDF documentation 


AssCool.py is a impletation of code Ass.py, it only requires python build-in modules tkinter and random to run.
In AssCool.py the class "Solitaire" of Ass.py has been modified, I limit the number of cards to 6. While you start a game, the random() will mix the number from 1 to 7 to make a randomlized cards:
'''python
    self.cards = random.sample(range(1, 7), 6)
    self.solitaire_game = Solitaire(self.cards)
'''
