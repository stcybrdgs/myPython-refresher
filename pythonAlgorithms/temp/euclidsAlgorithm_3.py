# euclidsAlgorithm_2.py
# a leaner version of the algorithm

# functions ===============================
def gcd(a, b):
	while( b != 0):
		t = a
		a = b
		b = t % b
	return a

# main ====================================
def main():
	a = (100, 8, 20, 256, 112)
	b = (25, 4, 12, 113, 8)
	z = zip(a, b)
	for i, j in z:
		print(f'a={i}, b={j}, gcd=', gcd(i, j))

if __name__=='__main__': main()