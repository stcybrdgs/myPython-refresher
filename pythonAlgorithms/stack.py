# stack.py
'''
-  stacks are a LIFO structure that support push() and pop()
-  push/pop and enque/deque are constant time operations
-  stacks are fundamental structures with broad practical applications
   in software development

-  STACK EXAMPLES:
-    one example of using a stack would be to evaluate a mathematical expression
     using reverse Polish notation
-    another example of using a stack is to provide a backtracking feature, such
     as when you follow links in your browser; if you push each link onto a stack,
     then backtracking just requires a pop()

'''

# classes =============================

# functions ===========================
	
# main ================================
def main():
	# in python you can just use a list to represent a stack or queue
	# make a stack
	stack = []
	print('Stack contents: ', stack)
	
	# push values onto stack
	val = 0
	while( len(stack) < 4 ):
		stack.append(val)
		val += 1
		print('Stack contents: ', stack)
	
	# pop values off stack 
	while ( len(stack) > 0 ):
		stack.pop() # pop value off stack
		print('Stack contents: ', stack)
	
	print('Done.')
	
if __name__ == '__main__' : main()