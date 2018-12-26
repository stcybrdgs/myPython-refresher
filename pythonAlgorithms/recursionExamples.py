# recursionExamples.py
'''
in its simplest form, recursion is when a function calls itself from within its own code;
this kind of pattern appears a lot in the real world when you need to repeat a process
ad infinitum until a solution is reached;
each time a process is called in the series, its arguments are stored to a call stack so that
the series of processes can collapse upon reaching the final process run (aka 'the
breaking condition');

'''
# imports ==============================

# globals ==============================

# classes ==============================

# functions ============================
def countdown(x):
	if x == 0:
		print('Countdown complete!')
		return
	else:
		print(x, '...')
		countdown(x-1)
	
# main =================================
def main():
	countdown(10)
	print('Done.')

if __name__ == '__main__' : main()	