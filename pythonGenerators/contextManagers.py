# contextManagers.py
'''
A context manager is a python object that is able to act as a control
structure when used after the 'with' statement. . . this means they
manage context for a caller.

A generator can provide a short-hand way of producing a context manager.

A context-manager function should look like this:

# Context Manager
@contextmanager
defsimple_cm(n):
    try:
	    # setup code
		yield # rem yield control back to caller
	finally:
	    # wrap up code
		
Context managers allow easy execution of setup code and wrap-up code
with the help of Python generators and the context manager decorator.

'''
# imports ============================
from contextlib import contextmanager

# functions ==========================
# the contextmanager decorator enhances the generator object;
# the contextmanager function takes an object as an argument
@contextmanager
def simple_context_manager(obj):
	try:
		obj.some_property += 1
		# rem 'yield' tells python that this function is a 
		# generator function (so, it will return a generator object)
		yield 
	finally:
		obj.some_property -= 1
		
# classes ============================
class Some_obj(object):
	def __init__(self, arg):
		self.some_property = arg

# main ===============================
def main():
	obj = Some_obj(5)
	print(obj.some_property)
	
	# use the context manager
	# note that the content of the with block will be executed
	# when the context manager yields control
	with simple_context_manager(obj):
		print(obj.some_property)
	
	print(obj.some_property)
		
	print('\n\nDone.')

if __name__=='__main__': main()