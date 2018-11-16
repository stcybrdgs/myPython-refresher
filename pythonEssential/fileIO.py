# file i/o

# main ==================
def main():
	# open a file and return a file object (here, 'f')
	# rem the file object itself is an iterator
	#     and can be operated upon with a loop 
	f = open('lines.txt', 'rt')     
	for line in f:
		# print(line)           # print each line including returns
		print(line.rstrip())  # print each line without returns
	f.close()
	
	# create read file object and write file object
	infile = open('lines.txt', 'rt')
	outfile = open('lines-copy.txt', 'wt')
		
	# use iterator with a loop to open the file one line at a time
	# without having to buffer the whole file in memory
	print('\nwriting to external file:')
	for line in infile:
		print(line.rstrip(), file=outfile) # equivalent method: outfile.writelines(line)
		print('.', end='', flush=True) # rem flush the output buffer
	outfile.close()
	infile.close()
	print('\nDone.')
	
	infile = open ('C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\this.py', 'rt')
	outfile = open('importThis.txt', 'wt')
	print('\nwriting to external file again:')
	for line in infile:
		outfile.writelines(line)
		print('.', end='', flush=True) # rem flush the output buffer
	outfile.close()
	infile.close()
	print('\nDone.')
	
    # open() takes argument
	# it opens a file as read-only and text mode by default
	# arg 'w' means 'write' mode
	# arg 'r' means 'read' mode
	# arg 'a' means 'append' mode
	# arg '+' may be added to any mode to allow both read and write (ie, 'a+')
	# arg 'b' may be added to any mode to allow binary mode (ie, 'a+b')
	# arg 't' may be added to any mode to allow text mode (ie, 'a+t')
	# rem in 'w' mode, the file is emptied if not already empty
	#     and then it's overwritten from the beginning of the file
	#     and if the file doesn't exist, then it's created
	# rem in 'a' mode, if the file has contents it is not emptied
	#     and any new content is appended to the end of the existing content


if __name__ == '__main__': main()