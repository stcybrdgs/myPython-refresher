#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    # in Python, the first argument for a method inside of a class is 'self'
    # but 'self' is not a keyword, and you can name it something else (ie, 'this')
    # the arg 'self' is a reference to the object when the class
    # is used to create an object. . .
    # so when you have multiple objects, Python makes a reference
    # to each instance through the 'self' argument
    # so that it can keep track of which object is using the
    # class attributes
    sound = 'Quaaack!'
    walking = 'Walks like a duck.'
    
    def quack(self):
        print('Quaaack!')
        print(self.sound)

    def walk(self):
        print('Walks like a duck.')
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
