# functions with key word arguments
# are like list arguments that are
# dictionaries instead of tuples
# rem such structures allow your function
# to have a variable number of named arguments


# functions ===========================
def dog(**kwargs):
	if len(kwargs):
		for k in kwargs:
			print('{} says {}'.format(k, kwargs[k]))
	else: print('The dogs are sleeping now.')
	

# main() =============================	
def main():
	# pass kv pairs to dogs(**kwargs)
	dog( JazzWinston = 'ruff', Rikki = 'bark' )
	
	# working with the contents of a dictionary
	myDogs = { 'JazzWinston' : 'ruff', 'Rikki' : 'bark' }
	
	# pass the pre-defined dictionary to dog(**kwargs)
	dog(**myDogs)
	
	# other ways to work with a dictionary
	# (rem lu the full library of python dictionary methods)
	# use array notation to get individual values of dictionary keys
	print('\nuse array notation to get individual values:')
	print( myDogs['JazzWinston'] )
	print( myDogs['Rikki'] )
	
	# use the dictionary's get() method to get individual values of keys
	print('\nuse get() to get individual values:')
	print( myDogs.get('JazzWinston') )
	print( myDogs.get('Rikki') )

	# use the dictionary's values() method to get values of all keys
	print('\nuse values() to get all values:')
	
	# use the dictionary's items() method to get all keys and values
	print('\nuse items() to get all keys and values:')
	print( myDogs.items() )


if __name__ == '__main__': main()

