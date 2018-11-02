# the 'shebang' line is a common pattern on Unix-based systems
# it allows a script to be invoked from the command line
# following the shebang is a path to the executable that will run
# the script, along with any optional arguments
#!/usr/bin/env python3


import platform

def main():
	# a STATEMENT is a unit of execution that may be an expression
	# an EXPRESSION is a combination of literals, identifiers, and operators
	# and is a unit of evaluation;
	# generally, anything that retunrs a value is an expression:
	# x = y        assignment
	# x * y        operation
	# (x, y)       an aggregate value (a tuple)
	# x            a simple value
	# True         a built-in constant value
	# f()          a function call

	version = format(platform.python_version())  # an expression
	print('This is python version {}', version)  # a statement

    # whitespace is significant in Python
	# and code blocks are indicated by indention rather than {}
	if ( 2 < 3 ):
		print('True')
	else:
		print('False')
		
	# there are no multi-line comments in Python


# by having a conditional statement that calls main()
# at the bottom of your document, it forces the interpreter
# to read the entire script before it runs any of the code
# which means you can put your functions in any order
# and this setup ensures they are all defined before being called 
if __name__=='__main__':
	main()


