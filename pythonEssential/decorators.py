# decorators
# A decorator is a form of metaprogramming and it can be described as a
# special type of function that returns a wrapper function

# imports ===============================


# functions =============================
# rem everything in python is an object, so a function is a type of object
# in f1(), we are using f1() as a wrapper for f2()
# so we can't get to it from main() unless we assign the object f1 to
# a variable and then use the variable to call its assigned object, ie
# var = f1(); var()
def f1():
	# print('this is f1()')
	print('this is not f2()')
	# create f2() within f1()
	# rem can't call f2() directly from main() bc it is scoped within f1()
	def f2():
		print('this IS f2()')
	return f2

def f3(f):
	def f4():
		print('this is before the f4() function call')
		f() # call the function assigned to the arg f
		print('this is after the f4()function call')
	return f4

def f5():
	print('this is f5()')
	
	
# main() ================================
def main():
	# start main
	x = f1   # assign the function object f1 to variable object x
	f1()     # use the function object to call the function
	         # and nothing appears in the console because f1()
	         # merely returns the object f2, it doesn't run f2()
	x()      # use the variable object to call the function
	         # and again nothing appears in the console because x
	         # is merely assigned to the f1 function object and not to
	         # its returned value
	y = f1() # here, we assign y to the f1 object's returned value
	         # which is function object f2
	         # but in addition to picking up the returned value,
	         # we also run any statements in f1()
	y()      # so, when we call y(), we are calling the function 
	         # that is returned by the function object f2, and now
	         # we see something in the console
	
	z = f3(f5)  # assign z to the return value of f3(),
	            # which is the object f4, which when it is called
	            # will run f4() as well as f(5) 
	z()         # use z object to call the function object it contains, ie f4
	
	# to see how this weird arrangement is executed with a decorator,
	# see py file decorators2.py

	

    
	



if __name__ == '__main__': main()


