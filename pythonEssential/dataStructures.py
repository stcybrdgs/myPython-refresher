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
	
# print the whole list, start to end
def printList(listArg):
	print('\nlist contents: ', end='')
	i = 0
	while (i < len(listArg)):
		i += 1
		if (i == len(listArg)):
			print(listArg[i-1], end='')
		else:
			print(listArg[i-1], ', ', end='')
	# print('\n')
	
# main() ================================
def main():
	guitar = []
	populateList(guitar)
	
	# print index items 1 and 2
	print('items guitar[1][2]: ', guitar[1], guitar[2])
	
	# print a slice of the list from one to three
	# rem the slice is non-inclusive of the ending index
	#     so, this statement effectively prints items 1 and 2
	#     as a 'slice' --> ['', '']
	print(guitar[1:3])

	# print a slice again, this time with a start, end, and step
	# parameter, just as you would do for a range of items
	print(guitar[0:3:2])
	
	# use index() to find the index location of 'Martin' in the list
	# and print it
	martinLoc = guitar.index('Martin')
	print(guitar[martinLoc])
	
	guitar.append('Eastman')   # add item to end of list
	guitar.insert(0, 'Strat')  # insert item at start of list
	printList(guitar)          # print list
	guitar.remove('Eastman')   # remove an item by value
	guitar.pop()	           # remove item from end by pop
	guitar.pop(0)              # pop by index
	del guitar[0]              # delete by index
	printList(guitar)          # print list
	
		
	
	


if __name__ == '__main__': main()


