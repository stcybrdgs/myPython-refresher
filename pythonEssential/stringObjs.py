# overview of string objects
# rem strings are objects and
# rem strings are first class objects in python 3


# imports =================


# classes =================
class MyString(str):       # rem str is the built-in string class in python
	def __str__(self):
		return self[::-1]  # reverse the string to read right to left


# functions ===============


# main() ==================
def main():
	
	s = 'hELLO, wORLD. . .  4 + 2 IS: {}'
	print(s.swapcase().format(4 + 2))
	
	myString = MyString('Hello, World.')
	print(myString)
	
	#
	# common string methods
	#
	print('\nSome common string methods: -----------------')
	s2 = ('Harry Dresden is a wizard')
	print(s2.upper(), '--> upper()')
	print(s2.lower(), '--> lower()')
	print(s2.capitalize(), '--> capitalize()')
	print(s2.title(), '--> title()')
	print(s2.swapcase(), '--> swapcase()')
	print(s2.casefold(), '--> casefold()') # removes all case distinctions, even in Unicode

	# rem a string in python is immutable, it cannot be changed
	# rem so when you use a transformation method, the returned string
	#     is actually a different object
	print('\nStrings are immutable, so string methods return new string objects: ')
	s4 = 'Bob the Skull is funny'
	s5 = s4.upper()
	print('s4 : {}'.format(s4), ', s4 id: {}'.format(id(s4)))
	print('s5 : {}'.format(s5), ', s5 id: {}'.format(id(s5)))
	
    #
	# formatting examples
	#
	print('\nformatting examples: ------------------')
	x, y = 10, 20
	print('x is {bb} and y is {cc}'.format( bb = x, cc = y ))
	
	# print left justified with 5 spaces and right justified with 5 spaces
	# rem the colon indicates that formatting instructions follow
	print('x is {0:<5} and y is {1:>5}'.format(x, y))
	
	# format a big number by adding commas
	print('x * y * 10000 is: {:,}'.format(x * y * 10000))
	
	# replace commas from previous example with periods
	print('x * y * 10000 is: {:,}'.format(x * y * 10000).replace(',', '.'))
	
	# format a big number by adding commas and decimals
	print('x * y * 10000 is: {:,f}'.format(x * y * 10000))
	
	# use previous example with only three decimal places
	print('x * y * 10000 is: {:,.3f}'.format(x * y * 10000))  # using format()
	print(f'x * y * 10000 is: {x*y*10000:,.3f}')              # using f string
	
	#
	# splitting and joining
	#
	# split() returns a list of words that comprise the string
	str = 'Harry Dresden and Murphy have a very tense working relationship.'
	print('\nExample of split():')
	print(str.split())
	
	print('\nExample of split() on the letter "a":')
	print(str.split('a'))
	
	print('\nExample of join()')
	# rem join() takes a list or tuple as its argument
	l = str.split()
	j = ':'.join(l)   # joins the contents of the split() list on the character ':'
	print(j)
	j2 = ' '.join(l)
	print(j2)         # joins the contents of the split() liston the character ' '
	

  
    

if __name__ == '__main__': main()