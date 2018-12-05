# fibonacciGen_alt.py
#
# this script creates a generator to yield the fibonacci sequence

# functions ==========================
def fibonacci_generator():
    trailing, leading = 0, 1
    while True:
        yield leading
        trailing, leading = leading, trailing + leading
     
# main ===============================
def main():
    # let user input size of Fibonacci sequence
    cap = input('How many values do you want in the sequence? ')
    cap = int(cap)

    # loop through Fibonnacci sequence using the generator
    print('\nGenerating the sequence...')
    fib = fibonacci_generator()
    for v in range(cap):
        print(next(fib), ' ', end = '')

    print('\n\nDone.')


if __name__=='__main__': main()
