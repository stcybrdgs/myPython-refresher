#!/usr/bin/env python3
# the 'shebang' line is a common pattern on Unix-based systems
# it allows a script to be invoked from the command line
# following the shebang is a path to the executable that will run
# the script, along with any optional arguments


import platform

def main():
	# a STATEMENT is a unit of execution that may be an expression
	# an EXPRESSION is a combination of literals, identifiers, and operators
	# and is a unit of evaluation;
	# generally, anything that retunrs a value is an expression:
	# x = y        assignment
	# x * y        operation
	# (x, y)       an aggregate value (a tuple)
	# x            a simple value
	# True         a built-in constant value
	# f()          a function call

	version = format(platform.python_version())  # an expression
	print('This is python version {}', version)  # a statement

    # whitespace is significant in Python
    # and code blocks are indicated by indention rather than {}

	if ( 2 < 3 ):
		print('True')
	else:
		print('False')
		
	# there are no multi-line comments in Python

    # use format() and {} with print() to insert variables into print statement
    # this approach functions like the mustache code you found in AngularJS
	x, y = 421, 73
	if x > y:
		print ('x < y: x is {} and y is {}'.format(x,y))
	else:
		print('y > x')
	
	# blocks do not define scope in Python,
	# but functions, objects, and modules do define scope
	# notice how the following block does not define scope for variable z
	x = 0
	if (x < y):
		z = 100
		print('x < y, but z is: {}'.format(z))
	
	# python still knows value of z because blocks do not define scope:
	print('z is: {}'.format(z))
	
	# however, if the IF condition had failed, then the IF statement would not have run
	# and Python would not have learned the value of z
	# in which case any subsequent references to z would have returned an error
	
	# you can put your if statement on one line, but it is harder to read
	if x < y: print('this is hard to read, but x is {} and y is {}'.format(x,y))
	
	# remember that Python does not have a switch or case statement
	# although you may mimic one with a dictionary
	def switch_demo(i):
		switcher={
			0:'Sunday',
			1:'Monday',
			2:'Tuesday',
			3:'Wednesday',
			4:'Thursday',
			5:'Friday',
			6:'Saturday'
			}
		return switcher.get(i,"Invalid day of week")

	print(switch_demo(1))
	
	# LOOPS ====================================
	print('.................')
	words = ['one', 'two', 'three', 'four', 'five']  # array
	
	# while loop
	print('while loop: ')
	n = 0  # sentinel value
	while(n < 5):
		print(words[n])
		n += 1 # increment to avoid infinite loop
	print('.................')
	
	# for loop
	print('for loop: ')
	for i in words:
		print(i)
	print('.................')
	
	print() # skip a line
	
	# FUNCTIONS ====================================
	# remember that functions are used: 
	# -- to create re-usable code
	# -- to break a program down into smaller, more manageable pieces
	# -- as methods and objects
	# example 1
	# call a function and pass an argument
	def f0(n=1):  # ensure defalt value for arg
		print('f0() was passed a value of: ', n)
		
	f0(500)
	
	# example 2
	# set variable = function
	# in this example, the print function prints 'None'
	# which is the absence of a value
	# because x has been assigned to a function that returns NOne (no value)
	def f1(n=1):
		print(n)
	
	x = f1(50)  # f1() is called when x is declared
	print('functions example 2: ', x) # print() shows x = None
		
	
	# example 3
	# in this example, the print function prints 100 for the value of x
	# because x has been assigned to a function that returns a value of n * 2
	def f2(n=1):
		print(n)
		return n * 2
	
	x = f2(50)  # f2() is called when x is declared
	print('functions example 3: ', x)

    # Python's end parameter in print()
	# by default, Python's print() function ends with a newline '\n'
	# but if you want to change that behavior, you can do so by using
	# the print() function's 'end' parameter
	print('this sentence will end with some space', end = '   ')
	print(', but this one will end with a new line')
	print('--> new line')

# by having a conditional statement that calls main()
# at the bottom of your document, it forces the interpreter
# to read the entire script before it runs any of the code
# which means you can put your functions in any order
# and this setup ensures they are all defined before being called 
if __name__=='__main__':
	main()


