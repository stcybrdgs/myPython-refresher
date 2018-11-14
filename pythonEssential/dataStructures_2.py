# data structures 2

# imports ===============================
from math import pi

# globals ===============================
# var to manage nesting level for the mixed structures section
dlevel = 0

# FUNCTIONS ##################################
# sets don't allow duplicates, so printing a set that contains a string
# returns an unordered list of the unique letters that comprise the string;
# if you want the set ordered, then use sorted (setName)
def print_set(setArg, sortType):
	if( sortType == 'ordered'):
		setArg = sorted(setArg)
	for x in setArg:
		print(x, end = ' ')
	print()

# print list comprehensions built off a single range
def print_list(listArg):
	for x in listArg:
		print(x, end = ' ')
	print()

# main() ================================
def main():
	#
	# SETS
	#
	# python has a data type for sets, which are lists that don't allow duplicate elements

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
	
	# return the members of set a that are not in set b:
	print('\nset a-b: ')
	print_set(a - b, 'ordered')
	
	# return the members of set a OR set b:
	print('\nset a | b: ')
	print_set(a | b, 'ordered')
	
	# return the members of set a XOR set b (in either but not both):
	print('\nset a ^ b: ')
	print_set(a ^ b, 'ordered')	
	
	# return the members in both set a AND set b:
	print('\nset a & b: ')
	print_set(a & b, 'ordered')

	
	#
	# List comprehension
	#
	# a list comprehension is a list created based on another list or iterator
	# here are some examples of list comprehensions built off a single range
	seq1 = range(11)
	seq2 = [(x * 2) for x in seq1]
	seq3 = [(x) for x in seq1 if x % 3 != 0]
	seq4 = [(x, x**2) for x in seq1]
	seq5 = [round(pi, x) for x in seq1]
	seq6 = {x: x**2 for x in seq1}  # use seq to make a dictionary
	seq7 = {x for x in 'solomongrundy' if x not in 'grundy'} # use seq to make a set
	
	# print the list comprehensions
	seqList = [seq1, seq2, seq3, seq4, seq5, seq6, seq7]
	count = 1
	while ( count <= 7):
		print('\nseq', count, ': ')
		print_list(seqList[count-1])
		count += 1
	
# end main()
if __name__ == '__main__': main()


