# python classes

# classes ===================================
class Guitar:
    sound = 'notes notes notes.'
    appearance = 'looks super awesome.'

    # rem self references the object instance of the class
    # that is being used to call the method
    def scale(self):
        print(self.sound)

    def body(self):
        print(self.appearance)

class Player:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre
    
    def name(self):
        return self._name
    
    def genre(self):
        return self._genre
    
def print_player(o):
    if not isinstance(o, Player):
        raise TypeError('print_player(): requires a Player')
    print('The player is named "{}" and is a {} player'.format(o.name(), o.genre()))

    
# main ===================================
def main():
    gibson = Guitar()
    gibson.scale()
    gibson.body()
    
    p1 = Player('Joe Pass', 'Jazz')
    p2 = Player('Joe Satriani', 'Rock')
    print_player(p1)
    print_player(p2)



if __name__ == '__main__': main()
