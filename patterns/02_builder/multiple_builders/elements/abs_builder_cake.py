import abc 
from cake import Cake


class AbsCakeBuilder(abs.ABC):
    
    def get_cake(self):
        '''return cake instance'''
        return self._cake 

    def new_cake(self):
        '''instantiate internal cake instance'''
        self._cake = Cake()
        
    @abc.abstractmethod
    def cook_cake_flavor(self): 
        pass

    @abc.abstractmethod
    def cut_shape(self): 
        pass
    
    @abc.abstractmethod
    def mount_cake(self): 
        pass
