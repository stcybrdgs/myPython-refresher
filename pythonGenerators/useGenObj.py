# useGenObj.py
'''
Using a generator ultimately means getting it to yield
values for you. A generator object has one method that
causes it to yield values, and that is the next() method.

When using generators, keep the following stuff in mind:
* generator objects cannot be reused
* calling next() on exhausted generator throws StopIteration exception
* python's for loop will handle StopIteration for you
* generator expressions may be passed directly to a function
* when passing a generator expression into a function call as an argument,
      you do not need an extra set of parentheses

'''
# functions ========================
def evenInts_generator(n):
	for i in range(n):
		if i % 2 == 0: yield i
	
# main =============================
def main():
	# store generator in ints
	ints = evenInts_generator(10)

	# get iterator and call next a few times
	print('using iterator -----------------')
	print(next(ints))
	print(next(ints))
	print(next(ints))
	print(next(ints))
	print(next(ints))

	# use python's for loop machinery to cycle through
	# entire generator sequence without throwing an
	# out-of-range exception
	print('\nusing for loop ---------------')
	ints2 = evenInts_generator(10)
	for i in ints2:
		print(i)
		
	# pass a call to the generator function directly
	# into a for loop
	print('\ncalling gen function from for loop -----')
	for n in evenInts_generator(10):
		print(n)
	
	# pass a generator expression into a for loop
	print('\npassing generator expression into a for loop ---')
	for n in (i for i in range(10)):
		print(n)
		
	# end
	print('Done.')
	
if __name__ == '__main__': main()

