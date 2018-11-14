# classes_2.py
# class methods
#
# rem python does not have private variables, so there's no way to actually prevent
# someone from using the class variables, but the self.__ is the conventional way to
# indicate that the variable should be treated as a private variable and that it should
# not be set or retreived outside of a setter or getter
#
class Animal:
    # class constructor
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'dog'
        self._name = kwargs['name'] if 'name' in kwargs else 'Jazz'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'bark'

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
