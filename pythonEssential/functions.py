# functions
# while some languages make a distinction between a
# function and a procedure, where a function returns a vaue
# and a procedure does not, python does not make that distinction;
# in python, all functions return a value, even if it is None,

# rem any arguments with defaults must occur after
# any arguments without defaults
# so that the interpreter can understand the arg list
# rem a good practice is to provide defaults for all args
# if any of them require a default
# (if you do it for one, do it for all)

# functions ===========================
def addInts(a, b=0, c=0):
	sum = a + b + c
	print(f'\n{sum}')

def subtractInts(a, b=0, c=0):
	sum = a - b - c
	return a
	
def addOne(arg):
	arg = arg + 1
	print('addOne(arg) is: ', arg)

def addTwo(arg):
	arg = arg + 2
	return arg

# python allows variable length argument lists
def kitten(*args):
	if len(args): # if arg length > 0
		for s in args:
			print(s)
	else: print('Meow')


# main() =============================	
def main():
	print('Main program')
	
	addInts(4)
	
	difference = subtractInts(1)
	print(difference)
	
	x = 1
	addOne(x)
	print('x is ', x)
	
	y = addTwo(x)
	print('y is ', y)
	
	# get user input for kitten sounds
	# and pass to kitten(*args)
	sound1 = input("Enter kitten sound 1: ")
	sound2 = input("Enter kitten sound 2: ")
	sound3 = input("Enter kitten sound 3: ")
	print('You entered: ')
	kitten(sound1, sound2, sound3)
	
	# print pre-defined list of kitten sounds
	# by passing a reference to a variable-length list
	# to kittens(*args)
	x = ( 'growl', 'hack', 'hiss' )
	kitten( *x )   

if __name__ == '__main__': main()

