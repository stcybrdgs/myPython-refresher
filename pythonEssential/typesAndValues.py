# this file is an overview of Python types and values

# import modules
from decimal import *

# some basic data types in Python
myTypeArray = [ 'Hello', 1, 7.0, .4e7, 2+3j, None, (True), True,
			   ('Volvo', 'Ford'), (1, 2, 3) ]
for i in myTypeArray:
	print('i is {}'.format(i), '  ', type(i))

# the above code example outputs the following basic types:
# str -       'Hello'	
# int -       1
# float -     7.0 or .4e7
# complex -   2+3j
# bool -      (True) or True
# tuple -     ('Volvo', 'Ford') or (1, 2, 3)

# in Python 3, all types (including built-in types) are classes
# also, regarding strings, Python treats single and double quotes the same
# in fact, if you use triple quotes, you can create a multi-line string
x = '''
seven,
eleven
'''
print(x)

# notice that an integer divided by an integer becomes a float:
print('\nExample: int/int = float :')
x = 7 / 3
print('x is: {}'.format(x))
print(type(x), '\n')

# notice the precision issue in the following calculation:
# (the computer sacrifices accuracy for precision, so it is not
# accurate, especially for money)
# DON'T USE FLOATING POINT FOR MONEY CALCULATIONS
# python comes with a built in module 'decimal' to help solve such issues
print('\nExample: (.1 + .1 + .1) - .3:')
x = (.1 + .1 + .1) - .3
print('x is {}'.format(x))
print(type(x), '\n')

# here is the above example again, but using the python decimal module:
print('\nExample using decimal module: (.1 + .1 + .1) - .3:')
a, b = Decimal('.10'), Decimal('.30')
x = (a + a + a) - b
print('x is {}'.format(x))
print(type(x), '\n')

# strings are objects, including literal strings, so you can run methods on it
x = 'seventy'
print( x.upper(), ', ', x.capitalize(), ', ', x + ' {} {}'.format(1, 2) )

# an example with auto-fill
print( x + ' : {1:<03} {0:>03}'.format(1, 2) )

# =================================
# examples using f strings
# ex 1: 
a, b = 8, 9
x = f'seven {a}{b}'
print( x )

# ex 2: the above f string is the same as:
a, b = 8, 9
x = 'seven {}{}'.format(a, b)
print( x )

# ex 3: ... is the same as:
a, b = 8, 9
x = 'seven'
print( x, '{}{}'.format(a, b) )

# ex 4: ... is the same as:
print( x, f'{a}{b}' )
# =================================

# re bool type, keep in mind that the following all evaluate as false:
# 0
# None
# ""

# python provides some built-in SEQUENCE types, including
# list, tuple, range, and dictionary
# rem list [], mutable
# rem tuple (), immutable
# rem range (), syntax: range(start, end, step)
# rem dictionary {}, mutable
# list example:
print('\nthis is the list example: ')
x = [ 1, 2, 3, 4, 5 ]  # this is a list-- it is mutable
x[2] = 42  # change value of second item in list to 42
for i in x:
	print('i is {}'.format(i))
#
# tuple example:
# consider always favoring the tuple structure unless your program
# will need to modify the contents, in which case use a list instead 
print('\nthis is the tuple example: ')
x = ( 1, 2, 3, 4, 5 )  # this is a list-- it is mutable
for i in x:
	print('i is {}'.format(i))
#
# you can also specify a sequence with range
# re range takes three parameters, but you don't have to use them all
# syntax w/ 1 parameters: range(endNum)
print('\nthis is the range example (1 parameters): ')
x = range(7)
for i in x:
	print('i is {}'.format(i))
#
# syntax w/ 2 parameters: range(startNum, endNum)
#
print('\nthis is the range example (2 parameters): ')
x = range(2,7)
for i in x:
	print('i is {}'.format(i))
#
# syntax w/ 3 parameters: range(startNum, endNum, stepByNum)
print('\nthis is the range example (3 parameters): ')
x = range(2, 7, 2)
for i in x:
	print('i is {}'.format(i))
#
# a dictionary is a searchable sequence of key value pairs using {}
# rem any item in the dictionary can be any data type
# rem a dictionary structure is mutable
print('\nthis is the dictionary example ========= ')
x = { 'one' : 1,
	  'two' : 2.0,
	  'three' : '3',
	  'four': 8/2,
	  'five' : .05E2
	}
x[3] = 9/3 # rem a dictionary is mutable
# print just the keys
print('just the keys are: ')
for i in x: # pull back just the keys
	print('i is {}'.format(i))
# print the keys with the values
print('\nthe keys with the values are: ')	
for k, v in x.items(): # pull back just the keys
	print('k: {}, v: {}'.format(k, v), ',', type(v))
	
# type() and id() ========================
# in python, everything is an object, so a Type is the same as a Class
# rem id() returns a unique identifier for each object
print('\nthis is the type() and id() example ================')
x, y = ( 1, 2, 3, 4, 5 ), ( 1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x), '/ type: ', type(x), ', id: ', id(x))
print('y is {}'.format(y), '/ type:', type(y), ', id: ', id(y))
#
print('\nnotice how the unique id for x[0], y[0] and x[4], y[4] are the same in the following sequences:')
print('types & ids for items in tuple X:')
# note that the i in the for loop automatically starts counting at 1
# instead of 0, so you will have to reset it to 0 if you want to
# recall an item from your list or dictionary from within the loop,
# otherwise the read activity will be looking for a memory block that
# is out of range and you'll get an error 
for i in x:
	print('item ', i, 'is a ', type(x[i-1]), ', ', id(x[i-1])) # set i counter to 0
#
print('\ntypes & ids for items in tuple Y:')
for i in x:
	print('item ', i, 'is a ', type(y[i-1]), ', ', id(y[i-1])) # set i counter to 0
#
print('\nis x[0] the same object as y[0]?')
if x[0] is y[0]:
	print('yes')
else:
	print('no')
print('\nis x[4] the same object as y[4]?')
if x[4] is y[4]:
	print('yes')
else:
	print('no')	
#
# to evaluate T/F for actual data type against proposed data type use
# isinstance()
print('\nis x a tuple?')
if isinstance(x, tuple):
	print('yes')
else:
	print('no')
print('\nis x a tuple?')
if isinstance(y, tuple):
	print('yes')
else:
	print('no')		
	

	
	

	


