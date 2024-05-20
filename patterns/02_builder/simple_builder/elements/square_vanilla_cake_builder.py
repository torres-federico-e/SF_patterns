from abs_builder_cake import AbsCakeBuilder


class SquareVanillaCakeBuilder(AbsCakeBuilder):
    '''Implements Square Vanilla Cake concretely defined here'''

    def cook_flavor(self): 
        '''steps to cook vainilla cake'''
        self.flavour = self.get_flavour('vainilla')

    def cut_shape(self): 
        '''steps to define concrete shape'''
        self.shape = self.get_shape('square')
    
    def mount_cake(self): 
        '''concrete mounting process steps'''
        self.mounted_cake = '\n'.join([self.shape, self.flavour])
        self.mounted_cake += '\n *** with Frosting ***'
