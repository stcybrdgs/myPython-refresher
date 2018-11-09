# decorators
# A decorator is a form of metaprogramming and it can be described as a
# special type of function that returns a wrapper function

# imports ===============================


# functions =============================
# f1 is the decorator function taking f3 as an argument
# as declared by the decorator syntax preceding f3 below
def f1(f):
	def f2():
		print('this is before the function call')
		f() # call the function assigned to the arg f
		print('this is after the function call')
	return f2

# using the decorator syntax, f3 is passed to f1
# so that now f3 can't be called directly but only through the wrapper
@f1
def f3():
	print('this is f3()')
	
	
# main() ================================
def main():
	# start main
	  
	f3()  # call f3 through the wrapper
	
	# to see how decorators can be useful in practice,
	# look at the file decorators3.py
	


if __name__ == '__main__': main()


