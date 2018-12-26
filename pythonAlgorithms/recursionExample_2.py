# recursionExample_2.py

# functions ============================
# this function returns num^pwr
def power(num, pwr):
	# breaking condition
	if pwr == 0:
		return 1
	else:
		return num * power(num, pwr-1)
'''	
# rem 0! = 1
# rem 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(num):
	if(num == 1):
		return
	else:
		num = num
'''		
	
# main =================================
def main():
	print('6^4 is: ', power(6,4))

	print('Done.')

if __name__ == '__main__' : main()	