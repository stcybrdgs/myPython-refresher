# python containers


# imports ===================


# functions =================


# main ======================
def main():
	# misc built-in functions
	# rem check out Built-in functions in the Python standard library
	x = ( 0, 1, 2, 3, 4, 5 )
	myFunctions = (
		x,
		type(x),
		id(x),
		len(x),
		reversed(x),
		list(reversed(x)),
		sum(x),
		sum(x, 10),
		min(x),
		max(x),
		any(x),  # return true if any are not 0
		all(x),  # return true if all are not 0
	)
	for item in myFunctions:
		print(item)
		
	# zipping tuples together
	print('\nzipping tuples:')
	u = (1, 2, 3, 4)
	v = (10, 20, 30, 40)
	z = zip(u, v)
	for a, b in z: print(f' {a} - {b}')
	
	# enumerating a tuple
	t = ('acoustic', 'nylon', 'electric', 'air')
	for i, v in enumerate(t): print(f'{i}: {v}')
	
	
if __name__ == '__main__': main()