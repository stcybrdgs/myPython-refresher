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
