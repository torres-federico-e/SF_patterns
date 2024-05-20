from vanilla_cake_builder import VanillaBuilder

class Director:
    '''Define process ('cook' the cake) '''

    def __init__(self, cake_builder, shape_builder) -> None:
        '''get/initialize respective builders'''
        self._flavor_builder = flavour_builder()
        self._shape_builder = shape_builder()

    def cook_cake(self) -> Cake: 
        self._flavor_builder.cook_sponge()
        self._shape_builder.cut_shape()
        self._shape_builder.mount_cake()
    
    def get_cake(self) -> Cake: 
        self._builder._get_cake()