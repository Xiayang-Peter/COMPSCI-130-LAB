from Class import CardPile
from Class import Solitaire


cards = [5, 13, 9, 6, 12, 8, 11, 14, 10, 7, 1, 2, 0, 3, 4]
game = Solitaire(cards)
game.get_pile(0).add_top(15)
game.get_pile(0).print_all(0)
game.get_pile(0).print_all(1)