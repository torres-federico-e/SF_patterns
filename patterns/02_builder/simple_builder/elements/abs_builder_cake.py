import abc 
from cake import Cake


class AbsCakeBuilder(abs.ABC):
    
    def new_cake(self):
        '''instantiate internal cake instance'''
        self._cake = Cake()

    def get_cake(self):
        '''return cake instance'''
        return self._cake 
    
    # helper function
    def load_template(path, element_type):
        '''loads Concrete Template types from path'''
        complete_file_path = os.path.join([path,element_type, '.txt'])
        with open(file_path, 'r') as file:
            return file.readlines()
    
    # helper function
    def get_shape(shape):
        path = './cakes_shape'
        self.load_template(path, shape)
        
    # helper function
    def get_flavour(flavour):
        path = './cakes_flavour'
        self.load_template(path, flavour)


    @abc.abstractmethod
    def cook_flavor(self): 
        pass

    @abc.abstractmethod
    def cut_shape(self): 
        pass
    
    @abc.abstractmethod
    def mount_cake(self): 
        pass
