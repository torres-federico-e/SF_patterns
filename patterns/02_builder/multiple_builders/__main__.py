from elements.director import Director
from elements.vainilla_cake_builder import SquareVanillaCakeBuilder

cooker = Director(SquareVanillaCakeBuilder)
cooker.cook_cake()
final_cake = cooker.get_cake()
print(final_cake)
