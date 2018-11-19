# itertools
# the itertools module allows us to iterate through data in different ways
# while helping you make your code more succinct and readable

import itertools

# main ========================
def main():
	# itertools.count()
	print('\nitertools.count() -------------')
	for x in itertools.count(50, 5): # (start, step)
		print(x)
		if x == 90: break
		
	# itertools.cycle()	
	print('\nitertools.cycle() -------------')
	count = 0
	for c in itertools.cycle('RACECAR'):
		print(c)
		count += 1
		if count > 50: break
	
	# itertools.repeat()
	print('\nitertools.repeat() -------------')
	count = 0
	for r in itertools.repeat(True):
		count += 1
		print(r)
		if count == 10: break
		
	
	# permutations
	# different ways of ordering a collection of things
	# example:
	# [1, 2, 3]    [1, 3, 2]
	# [2, 1, 3]    [2, 3, 1]
	# [3, 1, 2]    [3, 2, 1]
	#
	# rem for 3 things, num permutations = 3 * 2 * 1 = 6
	# rem for 4 things, num permutations = 4 * 3 * 2 * 1 = 24
	print('\nitertools.permutations() -------------')
	election = {1 : 'Jo', 2 : 'Ed', 3 : 'Mo', 4 : 'TJ'}
	
	# print key in election collection
	print('using dict keys:')
	for k in itertools.permutations(election):
		print(k)
	
	# print value in election collection
	print('\nusing dict values:')
	for v in itertools.permutations(election.values()):
		print(v)
	
	# combinations
	# order does not matter
	# no set has exact elements as another
	# (work, play, eat) --> (work, play) (work, eat) (play, eat)
	print('\nitertools.combinations() -------------')
	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
	# show possible combinations of 2 colors from colors[]
	for c in itertools.combinations(colors, 2):
		print(c)
		
	
if __name__ == '__main__': main()