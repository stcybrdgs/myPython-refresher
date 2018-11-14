# inheritance.py
#
#

# imports ====================================


# classes ====================================
# super class (base class, template)
class Animal:
    # class constructor
    # here, Animal is serving as a base class, so we aren't providing default values in the constructor
    # rem the base class isn't used directly, instead it is inherited in order to be used
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']
        
    # class methods
    # rem bc we aren't using default values, our setters/getters need to check to make sure that a value
    # already exists before trying to return it
    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

# child classes
class Cat(Animal):
    def __init__(self, **kwargs):
        if 'type' not in kwargs: self._type = 'Cat'
        super().__init__(**kwargs) # call and initialize parent class
    
class Dog(Animal):
    def __init__(self, **kwargs):
        if 'type' not in kwargs: self._type = 'Dog'
        super().__init__(**kwargs)    

class Pony(Animal):
    def __init__(self, **kwargs):
        if 'type' not in kwargs: self._type = 'Pony'
        super().__init__(**kwargs)
    
    def gait(self, g):
        print(f'{self.name()} will now travel at a {g}!')

# main() =======================================
def main():
    a0 = Cat(name = 'Mister', sound = 'Purr')
    a1 = Dog(name = 'Jazz', sound = 'Bark')
    a2 = Pony(name = 'Mr. Ed', sound = 'Neigh')
    
    barnyard = (a0, a1, a2)
    for a in barnyard:
        print(a)
    
    a2.gait('trot')
    a2.gait('gallop')
    
if __name__ == '__main__': main()
