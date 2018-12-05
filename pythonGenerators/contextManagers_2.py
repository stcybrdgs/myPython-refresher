# contextManagers.py
'''
A context manager has a yield statement that acts as a flow control device and
passes control back to the caller. But it also serves another purpose.
By putting a value to the right of 'the 'yield', the value is actually made available
inside the 'with' block of the caller.

'''
# imports ============================
from time import time
from contextlib import contextmanager

# globals ============================
HEADER = 'this is the header \n'
FOOTER = '\nthis is the footer\n'

# functions ==========================
@contextmanager
def new_log_file(name):
	try:
		logname = name
		outputFile = open(logname, 'w')
		outputFile.write(HEADER)
		yield outputFile # make output file available to caller
	finally:
		outputFile.write(FOOTER)
		print('logfile was created')
		outputFile.close()
		
# classes ============================

# main ===============================
def main():
	# the 'as shoe' statement makes use of the 'outputFile' value from yield
	# by storing it 'shoe' in the 'with' block...
	# you can interpret this block as
	# 'with whatever is returned from new_log_file('logfile'), name that
	# returned value shoe and then do something with it (in this case, write to it)'
	with new_log_file('logfile') as shoe: 
		shoe.write('this is the body')
		
	
	print('\n\nDone.')

if __name__=='__main__': main()