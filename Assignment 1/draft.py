from Class import CardPile
from Class import Solitaire

	
	
	
	
print("Testing Condition 3")
cards = [6, 2, 5, 4, 1, 3]
game = Solitaire(cards)
game.display()
game.move(0, 2)
game.move(0, 1)
game.move(0, 2)
game.move(0, 2)
game.move(0, 1)
print("AFTER 6 MOVES")
game.display()
game.move(1, 2)
print("AFTER INVALID MOVE (value of moving card not one less than bottom of pile)")
game.display()