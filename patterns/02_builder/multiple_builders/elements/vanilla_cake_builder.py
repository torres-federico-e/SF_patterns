from abs_builder_cake import AbsCakeBuilder


class SquareVanillaCakeBuilder(AbsCakeBuilder):
    '''Implements Vanilla Cake building method'''

    def __init__(self, shape_builder):
        self._shape_builder = ShapeBuilder
    
    def cook_cake_flavor(self): 
        self._flavour = 'vainilla'

    def cut_shape(self): 
        self._shape_builder.cut_shape()
    
    def mount_cake(self): 
        pass
