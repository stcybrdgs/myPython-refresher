# inheritance.py
#
#
class Animal:
    # class constructor
    # here, Animal is serving as a base class, so we aren't providing default values in the constructor
    # rem the base class isn't used directly, instead it is inherited in order to be used
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']
        
    # class methods
    # the following methods are both setters and getters
    # bc if no value is passed in, then they get the current existing value,
    # but if a value is passed in, then they set the value
    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
    
    # the __str__ method is a specially named method which provides the string representation of the object
    # (see more such specially named methods under Data Model in the python documentation)
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    # rem here we are encapsulating variable data, which means that it belongs to the object, not the class
    a0 = Animal(type = 'cat', name = 'Garfield', sound = 'meow')
    a1 = Animal(type = 'Duck', name = 'Howard', sound = 'Quack')
    a2 = Animal()
    print(a0)
    print(a1)
    print(a2)


if __name__ == '__main__': main()
