# handling exceptions #2
# exceptions are great for reporting runtime errors.
# it is best practice to generate your own exceptions
# for reporting errors in your code.


# imports ===============


# functions =============
def inclusive_range(*args):
	numargs = len(args)
	start = 0
	step = 1
	
	# initialize parameters
	if numargs < 1:
		raise TypeError(f'expected at least 1 argument, got {numargs}')
	elif numargs == 1:
		stop = args[0]
	elif numargs == 2:
		(start, stop) = args
	elif numargs == 3:
		(start, stop, step) = args
	else:
		raise TypeError(f'expected at most 3 arguments, got {numargs}')
	
	# generator
	i = start
	while i <= stop:
		yield i  # lu yield kw
		i += step
		

# main() ================
def main():
	try:
		for i in inclusive_range(1, 2, 3, 4):
			print(i, end = ' ')
		print()
	except TypeError as e:
		print(f'range error: {e}')
		
		
		
if __name__ == '__main__': main()	
