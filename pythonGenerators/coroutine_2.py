# coroutine_2.py
'''
Notice that most of the code for the example coroutine is set inside a 'try' block.
It is good practice to use a 'try' block for your code and end with an
'except GeneratorExit' block. The purpose of this setup is so that when you're done with
the coroutine, you can close it out, which will raise the generator exit exception.
By handling the exception, you can provide some action that you want to occur
upon closing the coroutine.

This example demontstrates how to use a coroutine function to use a coroutine function to
build objects that consume data and maintain internal state on an on-going basis.
'''
# functions ==========================
def counter(string):
	count = 0
	try:
		while True:
			item = yield
			if isinstance(item, str):
				if item in string:
					count += 1
					print('Match: ', item)
				else:
					print('No match: ', item)
			else:
				print('No match: ', item, ' is not a string.')
	except GeneratorExit:
		print('Total matches: ', count)

# main ===============================
def main():
	print('Running coroutine...\n')
	
	# create a coroutine object and pass in a comparitive string
	c = counter('This is the comparative string to be used by the coroutine.')
	
	# prime the coroutine
	next(c)
	
	# try sending in some strings to see if you get a match to the comparitive string
	stringList = ['This', 'is', 'chocolate', 'to', 'dog', 5, 'shoe', 'coroutine']
	for item in stringList:
		c.send(item)
	
	# close the coroutine to run the 'except GeneratorExit' block
	print('\nClosing coroutine...')
	c.close()
	
	print('\nDone.')


if __name__=='__main__': main()