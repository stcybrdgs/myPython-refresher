import myModule

def main():
	numObj = myModule.NumOps()
	print('11 + 2 is: ', numObj.add(11,2))
	print('11 - 2 is: ', numObj.subtract(11,2))
	print('11 * 2 is: ', numObj.multiply(11,2))
	print('11 / 2 is: ', numObj.divide(11,2))	

if __name__=='__main__':main()
