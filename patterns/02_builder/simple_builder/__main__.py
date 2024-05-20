from elements.director import Director
from elements.vainilla_cake_builder import SquareVanillaCakeBuilder

cake_director = Director(SquareVanillaCakeBuilder())
cake_director.cook_cake()
cake  = cake_director.get_cake()
cake.display()

