# recursionExample_2.py

# functions ============================
# this function returns num^pwr
def power(num, pwr):
	# breaking condition
	if pwr == 0:
		return 1
	else:
		return num * power(num, pwr-1)

# this function returns a factorial
# rem 0! = 1
# rem 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(num):
	if(num == 0):
		return 1
	else:
		return num * factorial(num - 1)
	
# main =================================
def main():
	# return the results of some power calculations:
	powerNums = (6, 4, 8, 2)
	powerPwrs = (4, 6, 9, 3)
	powerZip = zip(powerNums, powerPwrs)
	for n, p in powerZip:
		print(f'{n}^{p} is: ', power(n, p))
		
	# return the results of some factorial calculations:
	facNums = (5, 25, 6, 3)
	for i in facNums:
		print(f'{i}! is: ', factorial(i))

	print('Done.')

if __name__ == '__main__' : main()	