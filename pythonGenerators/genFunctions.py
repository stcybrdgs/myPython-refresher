# genFunctions.py
#
# python generatos are a great tool that make the
# creation of iterator objects as easy as writing
# a simple function. Iterators are objects that use a
# next() method to work with one item at a time when
# the item is needed, which makes for an efficient 
# allocation and use of storage space. When you are working
# with large amounts of data, this approach (aka 'lazy
# evaluation') allows you to evaluate one item at a time.
#
# the generator object is created when you call the function
# the term 'generator' by itself refers to the object
#
# Building a generator function is much like building
# any other function, but there's one important
# difference, which is the use of the keyword 'yield'. 

# functions ========================
# return a list of results that contains all even
# numbers that exist between 0 and n
def evenInts_function(n):
	result = [] # a list to contain the results
	for i in range(n):
		if i % 2 == 0: result.append(i)
	return result

# generators =======================
def evenInts_generator(n):
	for i in range(n):
		if i % 2 == 0:
			yield i
	
# main =============================
def main():
	# print result of list function
	list1 = [0, 2, 4, 6, 8]
	print(list1)
	
	# create and look at generator object
	gen1 = evenInts_generator(10) 
	print(gen1)
	
	# use generator object to print list
	# one item at a time
	print(list(gen1))
	
	# end
	print('Done.')
	
if __name__ == '__main__': main()

