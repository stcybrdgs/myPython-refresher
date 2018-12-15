# euclidsAlgorithm.py
'''
Some things to keep in mind when creating algorithms:

what is the space complexity? (how much memory does it take?)
what is the time complexity? (how much time does it take?)
what are the inputs and outputs?
what type of algortihm is it?
    -- serial / parallel
    -- exact / approximate
    -- deterministic / non-deterministic
    --    (non-deterministic are guesses that become more accurate over time)   

common algorithms:
    -- search (find something in a data set)
	-- sort (organize a data set)
	-- computational (take a set of data and derive a new set from it)
	-- collection (working with sets of data to aggregate, filter, etc.)
'''
# Euclid's algorithm finds the GCD of two ints
# ie, it finds the largest number that divides both ints with no remainder
# algorithm:
#     step 1: a = large number, b = small number
#     step 2: a%b, if r = 0 stop, if not next step
#     step 3: a = b, b = r
#     step 4: repeat steps 2 and 3 until r = 0

# globals =================================
big = 0
small = 0
remainder = 0

# functions ===============================
def getBigAndSmall(a,b):
	global big, small
	if(a > b):
		big = a
		small = b
	else:
		big = b
		small = a

def getRemainder():
	global big, small, remainder
	remainder = big%small
	
def getGCD(a,b):
	global big, small, remainder
		
	# step 1
	getBigAndSmall(a,b)
		
	# step 2
	getRemainder()
	if(remainder == 0):
		return
	
	# step 3
	else:
		big = small
		small = remainder
		# step 4
		getGCD(big, small)

# main ====================================
def main():
	line = '\n'
	a, b = 100, 25
	getGCD(a,b)
	print('a = {}, b = {}, gcd = {}'.format(a, b, small))
	print(line)
	print('Done')

if __name__=='__main__': main()

