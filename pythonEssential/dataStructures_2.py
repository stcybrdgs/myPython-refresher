# data structures 2
# python has a data type for sets, which are lists that don't allow duplicate elements

# imports ===============================


# FUNCTIONS ##################################
# sets don't allow duplicates, so printing a set that contains a string
# returns an unordered list of the unique letters that comprise the string;
# if you want the set ordered, then use sorted (setName)
def print_set(setArg, sortType):
	if( sortType == 'ordered'):
		setArg = sorted(setArg)
	for x in setArg:
		print(x, end = '')
		
# main() ================================
def main():
	# SETS
	a = set('I really enjoyed reading Stormfront.')
	b = set('Now I am reading Fool Moon.')
	
	print('set a: ')
	print_set(a, 'unordered')
	print('\nset b: ')
	print_set(b, 'ordered')
	
	# return the unique values of the set in set notation:
	print('\nset a: ')
	print(a)
	print('set b: ')
	print(b)
	
	# List comprehension
	
	# Mixed structures

	
	

# end main()
if __name__ == '__main__': main()


