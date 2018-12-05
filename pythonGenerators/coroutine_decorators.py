# coroutine_decorators.py
'''
to get around the need to prime a coroutine via next(), you can use
a decorator.
'''
# functions ======================		
def coroutine_decorator(func):
	# create a coroutine object and prime it with next()
	def wrap(*args, **kwargs):
		cr = func(*args, **kwargs)
		next(cr)
		return cr
	return wrap

@coroutine_decorator
def coroutine_example():
	while True:
		x = yield
		# do something with x
		print(x)

# main ===========================
def main():
	c = coroutine_example()
	c.send('Success!')
	# end
	print('Done.')

if __name__=='__main__': main()
