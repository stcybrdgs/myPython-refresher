# bubbleSort.py
'''
most modern languages have sorting algorithms built in, so you
won't necessarily have to write your own each time, but knowing
how they work will help you pick the best one; the most basic ones
are bubble sort, merge sort, and quick sort

- simple to understand and implement
- O(n^2) is the performance characterstic
- rem nested for loops usually have n^2 performance
- other sorting algorithms are generally better
- bubble sort is more of a teaching tool and not very practical for
  most real applications unless the data set is very small

'''
# functions ============================
def bubbleSort(data):
	for i in range(len(data) - 1, 0, -1):
		for j in range(i):
			if data[j] > data[j+1]:
				temp = data[j]
				data[j] = data[j+1]
				data[j+1] = temp
	
# main =================================
def main():
	bubbleArray = [6, 2, 4, 22, 1, 0, -1]
	print('Starting array: ', bubbleArray)
	bubbleSort(bubbleArray)
	print('Sorted array: ', bubbleArray)

	print('Done.')

if __name__ == '__main__' : main()	