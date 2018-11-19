# python statistics module

# imports
import statistics
import random

# functions

# main ======================
def main():
	agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]
	
	# mean (average of the values in the data array)
	print('mean is: ', statistics.mean(agesData))
	
	# median (midpoint in the data array)
	print('median is: ', statistics.median(agesData))
	
	# mode (most frequent value in the data array)
	print('mode is: ', statistics.mode(agesData))
	
	# variance (average of the squared differences from the mean)
	

if __name__ == '__main__': main()