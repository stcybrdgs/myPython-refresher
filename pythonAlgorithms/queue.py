# queue.py
'''
-  queues are a FIFO structure that support enqueing and dequeing
-  enque/deque are constant time operations
-  queues are fundamental structures with broad practical applications
   in software development

-  QUEUE EXAMPLES:	 
-    an example of using a queue is order processing because the FIFO queue ensures
     that orders will be filled in the order that they are received
-    another example of using a queue is message processing

-  DEQUE OBJECT:
     you can use a list as a queue in python, but the BigO becomes inefficient bc
     you have to shift all the contents down a slot when you dequeue an item, so you
     go from O(1) constant time to O(n) linear time in this scenario,
     which becomes very inefficient as the data set grows larger; instead, 
     it is more efficient to use the deque object from python's collections module

'''
# imports =============================
from collections import deque

# main ================================
def main():
	# make a queue
	queue = deque()
	
	# enque values
	val = 0
	while( len(queue) < 4 ):
		queue.append(val)
		val += 1
		print('Queue contents: ', queue)
		
	# deque values
	while( len(queue) > 0 ):
		queue.popleft() # take item off front of queue
		print('Queue contents: ', queue)
	
	print('Done.')
	
if __name__ == '__main__' : main()