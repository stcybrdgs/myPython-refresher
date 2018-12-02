# data structures
# python provides collection types for creating structured data
# list        []    a basic sequence                  mutable, ordered
# tuple       ()    a basic sequence                  immutable, ordered
# dictionary  {:}   list of key:value pairs           mutable, unordered, indexed, k:v 
# set         {}    unordered list of unique values   mutable, unordered, unindexed


# imports ===============================


# FUNCTIONS ##################################

# list functions =============================
def populateList(listArg):
	items = ['Benedetto', 'Collings', 'Martin', 'Gibson']
	i = 0
	while (i < len(items)):
		i += 1
		listArg.append(items[i-1])

# dictionary functions =============================
def populateDictionary(listArg):
	key = ['dog', 'cat', 'cow', 'duck']
	value = ['bark', 'meow', 'moo', 'quack']
	i = 0
	while (i < len(key)):
		i += 1
		listArg.update( { key[i-1]:value[i-1] } )	
		
def print_Dict(dir, name, dObj):
	if( dir == 'h' ):
		print('dictionary ', name, ': ', dObj)
	elif( dir =='v' ):
		print('dictionary ', name, ': ')
		for x in dObj:
			print(f'{x}:{dObj[x]}')
		# the other way to print key:value pairs is to use the item() method:
		# for k, v in dObj.items():
		#     print(f'{k}:{v}')
		
	else:
		print('invalid dictionary print direction.')
		
# main() ================================
def main():
	guitar = []
	populateList(guitar)
	
	#
	# LISTS 
	#
	print('\nLISTS =====================' )
	# locating items in a list --------------------------
	# print index items 1 and 2
	print('items guitar[1][2] --> ', guitar[1], guitar[2])
	
	# print a slice of the list from one to three
	# rem the slice is non-inclusive of the ending index
	#     so, this statement effectively prints items 1 and 2
	#     as a 'slice' --> ['', '']
	print('slice guitar[1:3] --> ', guitar[1:3])

	# print a slice again, this time with a start, end, and step
	# parameter, just as you would do for a range of items
	print('slice guitar[0:3:2] --> ', guitar[0:3:2])
	
	# use index() to find the index location of 'Martin' in the list
	# and print it
	martinLoc = guitar.index('Martin')
	print('locate by value --> ', guitar[martinLoc])
	
	
	# transforming items in a list ----------------------
	print('\ntransforming list. . .' )
	guitar.append('Eastman')   # add item to end of list
	guitar.insert(0, 'Strat')  # insert item at start of list
	print(','.join(guitar))   # print comma separated list
	
	print('\ntransforming list. . .' )
	guitar.remove('Eastman')   # remove an item by value
	guitar.pop()	           # remove item from end by pop
	guitar.pop(0)              # pop by index
	del guitar[0]              # delete by index
	print(','.join(guitar))    # print comma separatedlist
	
	#
	# DICTIONARIES 
	#
	print('\nDICTIONARIES ===============' )
	# you may create a dictionary with a basic declaration
	numbers = { 'one':1, 'two':2, 'three':3 }
	
	# you may create a dictionary with a dictionary constructor
	# and keyword arguments
	colors = dict( sky = 'blue', grass = 'green', sun = 'yellow' )
	
	# you may declare an empty dictionary and populate with
	# parallele arrays through a loop
	animals = {}
	populateDictionary(animals)
	
	# use print_dict(dir, name, dObj) to print you dictionaries
	# print horizontally
	print_Dict('h', 'numbers', numbers)
	print_Dict('h', 'colors', colors)
	print_Dict('h', 'animals', animals)
	
	# print vertically
	print_Dict('v', 'numbers', numbers)
	print_Dict('v', 'colors', colors)
	print_Dict('v', 'animals', animals)
	
	# print using items() method:
	print('dictionary animals (key:value):')
	for k, v in animals.items():
		print(f'{k}:{v}')
		
	# print just the keys using keys() method:
	print('dictionary animals (keys only):')
	for k in animals.keys():
		print(k)
		
	# print just the values using values() method:
	print('dictionary animals (values only):')
	for v in animals.values():
		print(v)		
	
	print('Cat says: ', animals['cat'])               # return value based on key
	animals['dog'] = 'Ruff!'                          # update a value based on key
	animals['lion'] = 'Rawr!'                         # add a new k:v pair
	print('Lion is in animals: ', 'lion' in animals)  # use IN to search for key
	print_Dict('h', 'animals', animals)
	
	# use get() method to see if a key is in a dictionary and return None if it isn't
	print(animals.get('Elephant'))
	
	

# end main()
if __name__ == '__main__': main()


