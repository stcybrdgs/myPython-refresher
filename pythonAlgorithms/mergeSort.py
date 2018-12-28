# mergeSort.py
'''
- merge sort is a 'divide and conquer' algorithm-- ie, it breaks data down into
  smaller parts that are easier to work with.
- it divides a single array into multiple arrays of one element each
- it uses recursion to sort the subarrays and build back up to the original data set
- it has a good performance profile in logarithmic time O(n log n)-- 'log linear'

'''
# imports =============================
# globals =============================
items = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]

# classes =============================
# functions ===========================
def mergesort(data):
	# break down the data set ------------------------
	# breaking condition occurs when the array contains only one element
	if len(data) > 1:
		mid = len(data)//2
		leftarray = data[:mid]
		rightarray = data[mid:]
		print(leftarray, ' ', rightarray)
		mergesort(leftarray)
		mergesort(rightarray)

		# merge the data sets ------------------------	
		i = 0 # left array index
		j = 0 # right array index
		k = 0 # merged array index
		# while both left and right arrays have content,
		# compare their values and sort from low to high
		# into the merged array 'k'
		while i < len(leftarray) and j < len(rightarray):
			if leftarray[i] < rightarray[j]:
				data[k] = leftarray[i]
				i += 1
			else:
				data[k] = rightarray[j]
				j += 1
			k += 1
		
		# if the left array still has values, sort them into k
		
		# if the right array still has values, sort them into k
		

		
# main ================================
def main():
	# find the mid point of the data set, then
	# show the original set and how it's been split up
	print('Show original set and first two splits: ')
	mid = len(items)//2
	print(items)
	print(items[:mid], ' ', items[mid:])
	print('\n')
	
	mergesort(items)

	
	# end
	print('Done.')

if __name__ == '__main__' : main()	