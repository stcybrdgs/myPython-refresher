# python statistics module

# imports
import statistics
import random
import math


# functions

# main ======================
def main():
	agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

	# mean (average of the values in the data array)
	print('mean is: ', statistics.mean(agesData))
	
	# median (midpoint location in the data array)
	print('median is: ', statistics.median(agesData))
	
	# mode (most frequent value in the data array)
	print('mode is: ', statistics.mode(agesData))
	
	# variance ======================
	# variance (average of the squared differences from the mean)
	# rem for each number in the array, subtract the mean and square the result
	#     then take the average of your results
	# (the variance tells you how varied your data is)
	# here, i built a variance array based on agesData and then took its average:
	print('\nvariance: ------------------')
	valMinusm2 = [10, 13, 14, 12, 11, 10, 11, 10, 15]
	m = statistics.mean(valMinusm2)
	index = 0
	for val in valMinusm2:
		valMinusm2[index] = ((valMinusm2[index]-m)**2)
		index += 1
	print(valMinusm2)
	index, finSum, myVarAvg = 0, 0, 0
	for val in valMinusm2:
		finSum = finSum + (valMinusm2[index])
		index += 1
	myVarAvg = finSum / len(valMinusm2)
	print('my variance for agesData: ', myVarAvg)
	print('python\'s variance for agesData: ', statistics.variance(agesData) )

	# standard deviation (a measure of how spread out numbers are)
	# rem square root of the variance
	print('\nstandard deviation: ------------------')
	print('my standard deviation for agesData: ', math.sqrt(myVarAvg))
	print('python\'s standard deviation for agesData: ', statistics.stdev(agesData))

if __name__ == '__main__': main()