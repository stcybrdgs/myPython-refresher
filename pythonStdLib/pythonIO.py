# python input/output
#
# Command Line Arguments
# this script is meant to run from the cmd line based on user-provided arguments
# rem open command line, navigate to file, enter 'python' 'nameOfFile' 'args', ie:
# >> python pythonIO.py 0 1 2

# the Seek Pointer:
# in all files, you have a seek pointer that points to a specific character in the file;
# the pointer keeps track of where you are in a document;
# before reading or writing, the pointer is set to location 0;
# the pointer will increment character by character as it reads or writes through a file;
# to reset the pointer, you may either close and reopen the file,
# or you may use the seek function, ie myFile.seek(0)

import sys

# Print Arguments
print('Number of arguments: ', len(sys.argv), 'arguments.')
print('Arguments ', sys.argv)

# Remove Arguments
# rem remove filename from args passed to script
sys.argv.remove(sys.argv[0])
print('Arguments', sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
	try:
		number = int(arg)
		sum = sum + number
	except Exception:
		print('Bad input')
print('\nThe sum of your arguments is: ', sum)

# get user input
color = input('What is your favorite color?')
print('\nYou selected the color: ', color)

# open a file and write user input to it
outFile = open('userColor.txt', 'w')
outFile.write('The user selected ' + color + '.')

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# show attributes and properties of the file
print('Name ' + outFile.name)
print('Mode ' + outFile.mode)

outFile.close()

# open a file and read from it
inputFile = open('userColor.txt', 'r')
print('Reading...\n' + inputFile.read())

inputFile.close()

# open the file again for more read/write operations
outFile = open('userColor.txt', 'a+')

# add some dictionary contents to the file
colorArray = {
	'color 1' : 'red',
	'color 2' : 'orange',
	'color 3' : 'green',
	'color 4' : 'blue',
	'color 5' : 'yellow',
	'color 6' : 'white',
	'color 7' : 'brown'
	}
print('\nWriting colorArray to file...')
for k, v in colorArray.items():
	outFile.write('\n%s : %s' % (k,v))
print('Done')

# reset the seek cursor
outFile.seek(0)

# read one line at a time
print('\nReading the outFile line by line...\n ')
for line in outFile:
	print(line.rstrip(), flush=True)

print('\nDone reading file. ')
outFile.close()
	
