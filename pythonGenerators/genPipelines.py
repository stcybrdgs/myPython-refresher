# genPipelines.py
'''
one approach to using generators is to link them together such that
each generator serves as one stage in a pipeline

Things to keep in mind when using pipleines:
* several pipes can be linked together
* items flow one by one through the entire pipeline
* pipeline functionality can be packaged into callable functions
'''
# main ===============================
def main():
	# use generator pipeline to find longest name in a file of names
	full_names = (name.strip() for name in open('names.txt'))
	lengths = ((name, len(name)) for name in full_names)
	longest = max(lengths, key = lambda x:x[1])
	
	print(f'The longest name is {longest[0]} at {longest[1]} chars.')
		
	print('\n\nDone.')

if __name__=='__main__': main()