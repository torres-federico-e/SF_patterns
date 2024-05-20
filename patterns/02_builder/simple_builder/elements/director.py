
class Director:
    '''Define build process (to 'cook' the cake) '''

    def __init__(self, cake_builder) -> None:
        '''get/initialize respective builders'''
        self._builder = cake_builder

    def cook_cake(self) -> None: 
        self._builder.new_cake()
        self._builder.cook_flavor()
        self._builder.cut_shape()
        self._builder.mount_cake()
    
    def get_cake(self) -> Cake: 
        return self._builder.get_cake()