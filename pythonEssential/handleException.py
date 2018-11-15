# handling exceptions

# imports ===============
import sys

# functions =============

# main() ================
def main():
	# use a try/except net to capture errors
	# rem the default except does not know what error might be captured
	# rem the default except must appear last in the set of exceptions
	try:
		# x = 1
		# x = int('foo')
		x = 5/0
	except ValueError:
		print('The script has captured a ValueError.')
	#except ZeroDivisionError:
	#	print('The script has captured a ZeroDivisionError.')
	except: # default
		# use sys to report on error details
		# use [1] index notation to pull the second indexed item from the list
		# of info that is returned by sys
		print(f'The script has caused an unknown error: {sys.exc_info()[1]}')
	else:
		print('The script appears to be error free.')
		print(x)
		
if __name__ == '__main__': main()	
