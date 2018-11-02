# an intro to Class and Class Objects in Python

# in Python, the first argument for a method inside of a class is 'self'
# but 'self' is not a keyword, and you can name it something else (ie, 'this')
# the arg 'self' is a reference to the object when the class
# is used to create an object. . .
# so when you have multiple objects, Python makes a reference
# to each instance through the 'self' argument
# so that it can keep track of which object is using the
# class attributes

class Dog:
    sound = 'Bark!'
    action = 'Wags like a dog.'
    
    def bark(self):
        print('Bark!')
        print(self.sound)

    def wag(self):
        print('Wags like a dog.')
        print(self.action)

def main():
    jazz = Dog()
    jazz.bark()
    jazz.wag()

if __name__ == '__main__': main()
