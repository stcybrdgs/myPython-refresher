# python classes

# classes ===================================
class Guitar:
    # class variables
    sound = 'notes notes notes.'
    appearance = 'looks super awesome.'

    # class methods
    # rem 'self' is used to reference the object instance of the class
    # that is being used to call the method
    def scale(self):
        print(self.sound)

    def body(self):
        print(self.appearance)

class Player:
    # class constructor __init__
    # rem first method is always self
    
    # class variables:
    def __init__(self, name = 'Stacy', genre = 'Instrumental'):
        self._name = name
        self._genre = genre
    
    # class methods:
    # rem accessors (aka getters) return values of object variables
    def getName(self):
        return self._name
    
    def getGenre(self):
        return self._genre
    
class ClothingItem:
    # if you don't want to have to remember the order in which args need to be
    # passed to your constructor, you can use **kwargs:
    
    # class variables:
    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name'] 
        self._color = kwargs['color'] 
    
    # class methods:
    def getType(self): return self._type
    def getName(self): return self._name
    def getColor(self): return self._color

class Band:
    # this class example uses **kwargs with default values
        
    # class variables:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Average'
        self._color = kwargs['color'] if 'name' in kwargs else 'White'        
        self._name = kwargs['name'] if 'name' in kwargs else 'Band'
    
    # class methods:
    def type(self): return self._type
    def name(self): return self._name
    def color(self): return self._color

# functions ===================================    
def print_player(o):
    if not isinstance(o, Player):
        raise TypeError('print_player(): requires a Player')
    print('The player is named "{}" and is a {} player'.format(o.getName(), o.getGenre()))

def print_clothingItem(o):
    if not isinstance(o, ClothingItem):
        raise TypeError('print_clothing(): requires a Clothing object')
    print('The article of clothing is for {} time and is a {} {}.'.format(o.getType(), o.getColor(), o.getName()))                        
    
def print_band(o):
    if not isinstance(o, Band):
        raise TypeError('print_band(): requires a Band object')
    print('The band is: {} {} {}.'.format(o.type(), o.color(), o.name()))
    
# main ===================================
def main():
    # Guitar() objects
    gibson = Guitar()
    gibson.scale()
    gibson.body()
    
    # Player() objects
    p1 = Player('Joe Pass', 'Jazz')
    p2 = Player('Joe Satriani', 'Rock')
    print_player(p1)
    print_player(p2)

    print(p1.getName(), ', ', p2.getName())

    # Clothing() objects
    c1 = ClothingItem(type = 'winter', name = 'boot', color = 'black')
    c2 = ClothingItem(type = 'summer', color = 'yellow', name = 'dress')

    print_clothingItem(c1)
    print_clothingItem(c2)
    
    # Band() objects
    b1 = Band(type = 'rock', name = 'Rush', color = 'white')
    b2 = Band()
    
    print_band(b1)
    print_band(b2)
    print_band(Band())
    
if __name__ == '__main__': main()