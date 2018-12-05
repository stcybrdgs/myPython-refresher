# fibonacciGen.py
#
# this script creates a generator to yield the fibonacci sequence

# globals ============================
aVal = 1
bVal = 1

# functions ==========================
def fibonacci_generator(maxVals):
    global aVal
    global bVal
    
    # if user-entered string is a number, convert to integer
    if( maxVals.isnumeric() ):
        cap = int(maxVals)
    # if user-entered string is not a number, throw an error and exit         
    else:
        print('Error: You must enter a non-negative integer value.')
        return
    # if user-entered string is 0 or negative, throw an error and exit
    if( cap == 0 ):
       print('Error: You must enter an integer greater than 0.')
       return
    
    for val in range(cap):
        if(val == 0 or val == 1):
            yield 1
        else:
            cVal = aVal + bVal
            aVal = bVal
            bVal = cVal
            yield cVal
     
# main ===============================
def main():
    # set a limit on the number of values in the Fibonacci sequence
    maxVals = input('How many values do you want in the sequence? ')

    # use for loop to print values yielded by Fibonnacci generator
    print('\nGenerating the sequence...')
    for vals in list(fibonacci_generator(maxVals)):
        print(vals, ' ', end = '')

    print('\n\nDone.')

if __name__=='__main__': main()
