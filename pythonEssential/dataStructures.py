# data structures
# python provides collection types for creating structured data
# list        []    a basic sequence                  mutable
# tuple       ()    a basic sequence                  immutable
# dictionary  {:}   list of key:value pairs           mutable 
# set         {}    unordered list of unique values   mutable


# imports ===============================


# functions =============================
# populate the list
def populateList(listArg):
	items = ['Benedetto', 'Collings', 'Martin', 'Gibson']
	i = 0
	while (i < len(items)):
		i += 1
		listArg.append(items[i-1])
	
		
# main() ================================
def main():
	guitar = []
	populateList(guitar)
	
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


# end main()
if __name__ == '__main__': main()


