# listComprehensions.py
#
# a list comprehension is an expression within a set of
# brackets that evaluates to a list
#
# list comprehesions are used to create new lists from
# other iterables
#
# they are usually more compact and faster than
# normal functions and loops for creating lists.
#      
	
# main =============================
def main():
	# list comprehensions
	# lc 1 -------------------------
	letters_1 = [ letter for letter in 'human' ]
	print( letters_1)
	
	# lc 2 -------------------------
	letters_2 = list( map(lambda x: x, 'human') )
	print(letters_2)
	
	# lc 3 -------------------------
	nums_1 = [
		x for x in range(20)
		if x % 2 == 0 ]
	print(nums_1)
	
	# lc 4 -------------------------
	nums_2 = [
		y for y in range(100)
		if y % 2 == 0
		if y % 5 == 0 ]
	print(nums_2)
	
	# lc 5 -------------------------
	obj = [
		"Even" if i%2==0
		else "Odd"
		for i in range(10) ]
	print(obj)
	
	# end
	print('Done.')
	
if __name__ == '__main__': main()

