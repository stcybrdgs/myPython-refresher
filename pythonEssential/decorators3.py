# decorators
# A decorator is a form of metaprogramming and it can be described as a
# special type of function that returns a wrapper function
# in this example from bill weinmann, a wrapper is being used to measure
# the time it takes to run a function

# imports ===============================
import time

# functions =============================
def elapsed_time(f):
	def wrapper():
		t1 = time.time()
		f()
		t2 = time.time()
		print(f'Elapsed time: {(t2 - t1) * 1000} ms')
	return wrapper
	
@elapsed_time
def big_sum():
	num_list = []
	for num in (range(0, 100000)):
		num_list.append(num)
	print(f'Big sum: {sum(num_list)}')
	
# main() ================================
def main():
	# start main
	big_sum()
	


if __name__ == '__main__': main()


